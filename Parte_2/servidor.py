# import grpc
import devices_pb2
# import ar_condicionado_pb2_grpc
from concurrent import futures
from socket import *
import threading
from abc import ABC, abstractmethod
from constants import *
import struct
import time
import multiprocessing as mp

import subprocess
import platform

class device_interface(ABC):

    @abstractmethod
    def handle_request(self , connection , addr):
        pass

"""OS DISPOSITIVOS SERÃO TODOS SERVIDORES , ENQUANTO O GATEWAY É TANTO CLIENTE DOS DISPOSITIVOS , QUANTO SERVIDOR
DE QUEM QUEIRA SE CONECTAR AO SISTEMA SERVINDO COMO A INTERFACE COM O MUNDO EXTERNO"""

class ar_condicionado(device_interface):

    def __init__(self , name : str ="Brastemp_Eletrolux" , on: bool = False, temperature : int = 20  ,
                 server_Name = gethostbyname(gethostname()) , server_Port = 50051  ) -> None:
        super(ar_condicionado , self).__init__()
        self.name = name
        self.temperature = temperature
        self.on = on
        
        self.server_Port = server_Port
        self.skt_Server  = socket( AF_INET , SOCK_STREAM )
        self.skt_Server.bind(( server_Name , server_Port ))
        self.skt_Server.listen(5)
        
        
        print("Server Ligado ", server_Name )
    
    def tcp_connect(self , timeout = 6):
        client , addr = None , None
        print("ar_condicionado aberto a novas conexões TCP")
        while True :
            try :
                self.skt_Server.settimeout(timeout)

                client , addr = self.skt_Server.accept()

                mp = mp.Process(target = self.handle_request , args=(client, addr))
                mp.start()

            except error as e:
                # Tratamento de exceção para liberar a thread em caso de interrupção
                print("tempo de espera por novas conexões em ar_condicionado encerrado ")
                
                return
            

    def send_info_2_multicast(self , timer = 10):
        # Criação de um socket UDP
        sock = socket( AF_INET , SOCK_DGRAM , IPPROTO_UDP )

        # Vincula o socket a um endereço e porta local
        # server_address = ("", port )
        # sock.bind( server_address )

        # Configura o socket para enviar dados para o grupo multicast
        group = inet_aton( multicast_group )
        mreq = struct.pack( "4sL", group , INADDR_ANY )
        sock.setsockopt( IPPROTO_IP , IP_ADD_MEMBERSHIP, mreq )
        # sock.setsockopt( IPPROTO_IP , IP_MULTICAST_TTL , 8 )
        
        try:
            print("O dispositivo iniciou a tentativa de estabelecer conecção via multicast e permanecerá tentando pelos próximos 1 minuto")
            # message = f"{self.server_Port} , ar_condicionado , {self.name}"
            message = devices_pb2.device_discover()
            message.name = self.name
            message.port = self.server_Port
            message.device_type = "ar_condicionado"

            start_time = time.time()
            while True:
                
                sock.sendto(message.SerializeToString() , (multicast_group, port))
                time.sleep(1)
                if (time.time() - start_time) > timer :
                    break
            print("Servidor multicast encerrado.")
        except KeyboardInterrupt:
            print("Servidor multicast encerrado.")
        finally:
            sock.close()
    def conect_in_localhost_devices(self , timer = 4):
        
        self.exit_thread = False
        td1 = threading.Thread(target= self.send_info_2_multicast , args=(timer,))
        td1.start()

        td2 = threading.Thread(target= self.tcp_connect , args=(timer,))
        td2.start()


    def handle_request(self , connection , addr):
        print("[NOVA Conexão em..  ar_condicionado ]")

        while True :
            data = connection.recv(1024)
            if data :

                request = devices_pb2.info_request()
                request.ParseFromString(data)

                # Roteie a mensagem com base nas informações do cabeçalho
                
                if  request.service  == "ar_condicionado" and request.method == "ar_condicionado_status":
                    response = devices_pb2.ar_condicionado_info()
                    response.on =  self.on
                    response.temperature =  self.temperature

                elif request.service == "ar_condicionado" and request.method == "ar_condicionado_on"  :
                    self.on = True
                    response = devices_pb2.ar_condicionado_info()
                    response.on =  self.on
                    response.temperature =  self.temperature
                elif request.service == "ar_condicionado" and request.method == "ar_condicionado_off" :
                    self.on = False
                    response = devices_pb2.ar_condicionado_info()
                    response.on =  self.on
                    response.temperature =  self.temperature
                elif request.service == "ar_condicionado" and request.method == "ar_condicionado_temp" :
                    self.temperature = request.new_temp
                    response = devices_pb2.ar_condicionado_info()
                    response.on =  self.on
                    response.temperature =  self.temperature
                elif request.service == "ar_condicionado" and request.method == "close_connection" :
                    connection.close()
                    return
                else:
                    print("Serviço ou método desconhecido")

                # f"Hello, {request.name}!The ar condicionado {request.name} is on now ."
                
                connection.send(response.SerializeToString())
                # connection.close()
                # return

    def __str__(self) -> str:
        return f"ar_condicionado() : {self.name} , temperature : {self.temperature} , on : {self.on}"
    

class gateway_server_skt():
    def __init__(self , server_Name = gethostbyname(gethostname()) , server_Port = 50051 , max_conections = 5) -> None:
        # server_Name = '/path/to/my/socket'
        self.skt_Server  = socket(AF_INET , SOCK_STREAM)
        self.skt_Server.bind((server_Name , server_Port))
        self.skt_Server.listen(max_conections)
        self.devices = {}

        print("Server Ligado ", server_Name )
    
    def find_devices(self) :
        # Criação de um socket UDP
        sock = socket(AF_INET, SOCK_DGRAM , IPPROTO_UDP)

        # Configura o socket para receber dados do grupo multicast
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL , 32) 
        sock.setsockopt(IPPROTO_IP, IP_MULTICAST_LOOP, 1)
        # sock.bind(("", port + rd.randint(1,13000)))
        sock.bind(("", port ))
        

        # Adiciona o cliente ao grupo multicast
        mreq = inet_aton(multicast_group) + inet_aton("0.0.0.0")
        sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

        # sock.listen(2)
        start_time = time.time()
        while True:

            print("Iniciando a busca em multicast")

            raw_data, address = sock.recvfrom(1024)
            # print(sock.recvfrom(1024))

            data = devices_pb2.device_discover()
            data.ParseFromString(raw_data)
            
            print(f"Recebido: \n{data} de {address}")
            self.devices[data.name] = data

            if (time.time() - start_time) > 6 :
                    print("Busca por devices encerrada")
                    break
        
        self.devices = { i.name:client_socket.connect((address[0], i.port )) for i in self.devices }
        print(self.devices)
    
    def handle_request(self , connection , addr):
        print("[NOVA Conexão..]")

        while True :
            data = connection.recv(1024)
            if data :

                request = devices_pb2.use_request()
                request.ParseFromString(data)

                # Roteie a mensagem com base nas informações do cabeçalho
                
                if  request.service  == "ar_condicionado" and request.method == "ar_condicionado_status":
                    data = devices_pb2.info_request()
                    data.service  = request.service
                    data.method   = request.method
                    data.name     = request.name
                    # data.new_temp = int(request.args)

                    self.devices[request.device_name].send(data.SerializeToString())
                    data = self.devices[request.device_name].recv(1024)

                    connection.send(data)
                    
                elif request.service == "ar_condicionado" and request.method == "ar_condicionado_on"  :
                    data = devices_pb2.info_request()
                    data.service  = request.service
                    data.method   = request.method
                    data.name     = request.name
                    # data.new_temp = int(request.args)

                    self.devices[request.device_name].send(data.SerializeToString())
                    data = self.devices[request.device_name].recv(1024)

                    connection.send(data)

                elif request.service == "ar_condicionado" and request.method == "ar_condicionado_off" :
                    data = devices_pb2.info_request()
                    data.service  = request.service
                    data.method   = request.method
                    data.name     = request.name
                    # data.new_temp = int(request.args)

                    self.devices[request.device_name].send(data.SerializeToString())
                    data = self.devices[request.device_name].recv(1024)

                    connection.send(data)

                elif request.service == "ar_condicionado" and request.method == "ar_condicionado_temp" :
                    data = devices_pb2.info_request()
                    data.service  = request.service
                    data.method   = request.method
                    data.name     = request.name
                    data.new_temp = int(request.args)

                    self.devices[request.device_name].send(data.SerializeToString())
                    data = self.devices[request.device_name].recv(1024)

                    connection.send(data)
                elif request.service == "ar_condicionado" and request.method == "close_connection" :
                    data = devices_pb2.info_request()
                    data.service  = request.service
                    data.method   = request.method
                    data.name     = request.name

                    self.devices[request.device_name].send(data.SerializeToString())
                    self.devices[request.device_name].close()
                    # self.devices[request.device_name] = "Conexão fechada"
                    # connection.close()
                elif request.service == "close":
                    connection.close()
                    return
                else:
                    print("Serviço ou método desconhecido")

                """print(f"O data recebido foi :\n{data}\n\nO request do data ficou :\n{request.name}")
                response = ar_condicionado_pb2.ar_condicionado_info()
                response.temperature = 3
                response.on = True
                # f"Hello, {request.name}!The ar condicionado {request.name} is on now ."
                
                connection.send(response.SerializeToString())
                connection.close()
                return"""

    def start_server(self):
        # listen()
        print("[Server Ouvindo...]")
        while True:
            
            client , addr = self.skt_Server.accept()
            
            td = threading.Thread(target = self.handle_request , args=(client, addr))
            td.start()

class cls():
    def __init__(self , server_Name = gethostbyname(gethostname()) , skt_Port = 50151 , max_conections = 5) -> None:
        self.skt_Server  = socket(AF_INET , SOCK_STREAM)
        self.skt_Port = skt_Port
        self.skt_Server.bind((server_Name , self.skt_Port))
        self.server_Name = server_Name
        # self.skt_Server.listen(max_conections)

    def prompt(self ,server_Name = gethostbyname(gethostname()) ,  port_to_connect = 50051):
        # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.skt_Server.connect(( server_Name , port_to_connect ))

        screen_msg = "Tipos de Dispositivos Disponíveis :\n\n1-ar_condicionado\n- \nMétodos Disponíveis :\n"
        msg2 = "\n1-ar_condicionado_status\n2-ar_condicionado_on\n3-ar_condicionado_off\n4-ar_condicionado_temp\n5-close_connection\n6-close"#

        screen_msg += msg2
        while True:
            print(screen_msg)
            # print("")
            device_type = ""
            while True :
                device_type = input("Digite o número do tipo de dispositivo que você quer interagir : ").strip().lower()
                if device_type.isnumeric():
                    device_type = int(device_type)
                    if (1 <= device_type) and (device_type <=1) :
                        break
                    else :
                        print("Digite um número dentro do range válido")
                else :
                    print("Input Inválido")
            
            device_name = input("Digite o nome do dispositivo que você quer interagir : ").strip().lower()
            print("Para usar alguma das funcionalidades do dispositívo digite o respectivo número ao envéz de um comando")
            comando = input("Digite um comando (cls ou clear para limpar a tela, sair para encerrar): ").strip().lower()

            if comando.isnumeric() :
                message  = devices_pb2.use_request()
                message.device_name   = device_name
                
                if device_type == 1 :
                    message.service  = "ar_condicionado"
                else :
                    print("Dispositivo inválido")

                if   int(comando) == 1 :
                    message.device_method = "ar_condicionado_status"
                    message.method = "ar_condicionado_status"
                elif int(comando) == 2 :
                    message.device_method = "ar_condicionado_on"
                    message.method = "ar_condicionado_on"
                elif int(comando) == 3 :
                    message.device_method = "ar_condicionado_off"
                    message.method = "ar_condicionado_off"
                elif int(comando) == 4 :
                    message.device_method = "ar_condicionado_temp"
                    message.method = "ar_condicionado_temp"
                    args = ""
                    while True :
                        args  = input("Qual a nova temperatura ? : ").strip().lower()
                        if args.isnumeric():
                            break
                        else :
                            print("Input Inválido")
                    message.args = args

                elif int(comando) == 5 :
                    message.device_method = "close_connection"
                elif int(comando) == 6 :
                    message.device_method = "close"

                self.skt_Server.send(message.SerializeToString())

            elif comando == "sair":
                break
            elif comando == "cls" and platform.system() == "Windows":
                # Limpar a tela no Windows
                subprocess.run("cls", shell=True)
            elif comando == "clear" and platform.system() != "Windows":
                # Limpar a tela em sistemas Unix-like (Linux, macOS)
                subprocess.run("clear", shell=True)
            else:
                print("Comando não reconhecido.")


        """request = devices_pb2.use_request()
        request.device_name   = "Brastemp-Eletrolux_X86"
        request.device_method = "ar_condicionado_temp"
        request.args = "2"

        request.service = "ar_condicionado"  
        request.method  = "ar_condicionado_temp"
        
        client_socket.send(request.SerializeToString())

        data = client_socket.recv(1024)
        response = ar_condicionado_pb2.ar_condicionado_info()
        response.ParseFromString(data)"""

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("localhost", 50051))
    server_socket.listen(5)

    print("Servidor socket em execução...")

    while True:
        client_socket, _ = server_socket.accept()
        data = client_socket.recv(1024)
        
        request = ar_condicionado_pb2.info_request()
        request.ParseFromString(data)
        print(f"O data recebido foi :\n{data}\n\nO request do data ficou :\n{request.name}")
        response = ar_condicionado_pb2.ar_condicionado_info()
        response.temperature = 3
        response.on = True
        # f"Hello, {request.name}!The ar condicionado {request.name} is on now ."
        
        client_socket.send(response.SerializeToString())
        client_socket.close()

if __name__ == "__main__":
    # main()
    # ar = ar_condicionado(server_Port = 50370)
    # ar.open_multicast_connection()

    # gateway = gateway_server_skt()
    # gateway.find_devices()

    pass

