import grpc
import ar_condicionado_pb2
import ar_condicionado_pb2_grpc
from concurrent import futures

class ar_condicionado(ar_condicionado_pb2_grpc.ar_condicionadoServicer):
    def ar_condicionado_on(self, request, context):
        response = ar_condicionado_pb2.ar_condicionado_info()
        response.message = f"Hello, {request.name}!The ar condicionado {request.name} is on now ."
        return response
    
    def ar_condicionado_off(self, request, context):
        response = ar_condicionado_pb2.ar_condicionado_info()
        response.message = f"Hello, {request.name}!The ar condicionado {request.name} is off now ."
        return response
    
    def ar_condicionado_status(self, request, context):
        response = ar_condicionado_pb2.ar_condicionado_info()
        response.message = f"Hello, {request.name}!"
        return response
    
    def ar_condicionado_temp(self, request, context):
        response = ar_condicionado_pb2.ar_condicionado_info()
        response.message = f"Hello, {request.name} the new temperature is {request.new_temp}!"
        return response

def main():
    # server = grpc.server(grpc.insecure_port("[::]:50051"))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    ar_condicionado_pb2_grpc.add_ar_condicionadoServicer_to_server(ar_condicionado(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC em execução...")
    server.wait_for_termination()

if __name__ == "__main__":
    main()
