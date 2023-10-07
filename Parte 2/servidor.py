# import grpc
import ar_condicionado_pb2
# import ar_condicionado_pb2_grpc
from concurrent import futures
from socket import *
import threading
# from overloading import override , overload
from dataclasses import dataclass
from abc import ABC, abstractmethod

class device_interface(ABC):

    @abstractmethod
    def handle_request(self , connection , addr):
        pass

"""OS DISPOSITIVOS SERÃO TODOS SERVIDORES , ENQUANTO O GATEWAY É TANTO CLIENTE DOS DISPOSITIVOS , QUANTO SERVIDOR
DE QUEM QUEIRA SE CONECTAR AO SISTEMA SERVINDO COMO A INTERFACE COM O MUNDO EXTERNO"""

class ar_condicionado(device_interface):

    def __init__(self , name : str ="Brastemp_Eletrolux" , on: bool = False, temperature : int = 20  ,
                 server_Name = gethostbyname(gethostname()) , server_Port = 50051) -> None:
        super(ar_condicionado , self).__init__()
        self.name = name
        self.temperature = temperature
        self.on = on

        self.skt_Server  = socket(AF_INET , SOCK_STREAM)
        self.skt_Server.bind((server_Name , server_Port))
        self.skt_Server.listen(5)
        
        print("Server Ligado ", server_Name )
    
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
    main()

