# import grpc
import devices_pb2
# import ar_condicionado_pb2_grpc
from concurrent import futures
from socket import *
import threading
# from overloading import override , overload
# from dataclasses import dataclass
from abc import ABC, abstractmethod
from constants import *
import struct
import time
# import random as rd

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
    
    def open_multicast_connection(self):

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
                # Envia a mensagem para o grupo multicast
                # sock.sendto(message.encode("utf-8"), (multicast_group, port))
                sock.sendto(message.SerializeToString() , (multicast_group, port))
                time.sleep(1)
                if (time.time() - start_time) > 10 :
                    break
            print("Servidor multicast encerrado.")
        except KeyboardInterrupt:
            print("Servidor multicast encerrado.")
        finally:
            sock.close()


    def handle_request(self , connection , addr):
        pass

    def __str__(self) -> str:
        return f"ar_condicionado() : {self.name} , temperature : {self.temperature} , on : {self.on}"
    

class gateway_server_skt():
    def __init__(self , server_Name = gethostbyname(gethostname()) , server_Port = 50051) -> None:
        # server_Name = '/path/to/my/socket'
        self.skt_Server  = socket(AF_INET , SOCK_STREAM)
        self.skt_Server.bind((server_Name , server_Port))
        self.skt_Server.listen(5)
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
            # data = data.decode('utf-8').strip().split(",")
            print(f"Recebido: \n{data} de {address}")
            if (time.time() - start_time) > 6 :
                    print("Busca por devices encerrada")
                    break
    
    def handle_request(self , connection , addr):
        print("[NOVA Conexão..]")

        while True :
            data = connection.recv(1024)
            if data :

                request = ar_condicionado_pb2.info_request()
                request.ParseFromString(data)

                # Roteie a mensagem com base nas informações do cabeçalho
                
                if  request.service  == "ar_condicionado" and request.method == "ar_condicionado_status":
                    response = meuservico_pb2.Response()
                    response.message =  "Chamou ServicoA MetodoA"
                elif request.service == "ar_condicionado" and request.method == "ar_condicionado_on"  :

                    response = meuservico_pb2.Response()
                    response.message =  "Chamou ServicoB MetodoB"
                elif request.service == "ar_condicionado" and request.method == "ar_condicionado_off" :
                    response = meuservico_pb2.Response()
                    response.message =  "Chamou ServicoB MetodoB"
                elif request.service == "ar_condicionado" and request.method == "ar_condicionado_temp" :
                    response = meuservico_pb2.Response()
                    response.message =  "Chamou ServicoB MetodoB"
                else:
                    response = meuservico_pb2.Response()
                    response.message =  "Serviço ou método desconhecido"

                print(f"O data recebido foi :\n{data}\n\nO request do data ficou :\n{request.name}")
                response = ar_condicionado_pb2.ar_condicionado_info()
                response.temperature = 3
                response.on = True
                # f"Hello, {request.name}!The ar condicionado {request.name} is on now ."
                
                connection.send(response.SerializeToString())
                connection.close()
                return

    def start_server(self):
        # listen()
        print("[Server Ouvindo...]")
        while True:
            
            client , addr = self.skt_Server.accept()
            
            td = threading.Thread(target = self.handle_request , args=(client, addr))
            td.start()


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

