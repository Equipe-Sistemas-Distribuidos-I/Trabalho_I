import time
from servidor import ar_condicionado , gateway_server_skt
# import threading

temperatura = 30
iluminado = False

#LOOP 

"""while True:
    #SIMULA O COMPORTAMENTO DE  TODOS OS DISPOSITIVOS :
    pass
    time.sleep(5)"""


# ar = ar_condicionado(server_Port = 5037)
# # ar.open_multicast_connection()

# td = threading.Thread(target = ar.open_multicast_connection , args=())
# td.start()

gateway = gateway_server_skt()
gateway.find_devices()

# td1 = threading.Thread(target = gateway.find_devices , args=())
# td1.start()

