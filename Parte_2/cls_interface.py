import devices_pb2
from socket import *
# import threading
from constants import *


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

# cmd = cls()
# cmd.prompt(port_to_connect = 50051)