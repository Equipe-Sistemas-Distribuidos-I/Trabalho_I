# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ar_condicionado_pb2 as ar__condicionado__pb2


class ar_condicionadoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ar_condicionado_on = channel.unary_unary(
                '/ar_condicionado/ar_condicionado_on',
                request_serializer=ar__condicionado__pb2.info_request.SerializeToString,
                response_deserializer=ar__condicionado__pb2.ar_condicionado_info.FromString,
                )
        self.ar_condicionado_off = channel.unary_unary(
                '/ar_condicionado/ar_condicionado_off',
                request_serializer=ar__condicionado__pb2.info_request.SerializeToString,
                response_deserializer=ar__condicionado__pb2.ar_condicionado_info.FromString,
                )
        self.ar_condicionado_status = channel.unary_unary(
                '/ar_condicionado/ar_condicionado_status',
                request_serializer=ar__condicionado__pb2.info_request.SerializeToString,
                response_deserializer=ar__condicionado__pb2.ar_condicionado_info.FromString,
                )
        self.ar_condicionado_temp = channel.unary_unary(
                '/ar_condicionado/ar_condicionado_temp',
                request_serializer=ar__condicionado__pb2.change_temp.SerializeToString,
                response_deserializer=ar__condicionado__pb2.ar_condicionado_info.FromString,
                )


class ar_condicionadoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ar_condicionado_on(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ar_condicionado_off(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ar_condicionado_status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ar_condicionado_temp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ar_condicionadoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ar_condicionado_on': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_on,
                    request_deserializer=ar__condicionado__pb2.info_request.FromString,
                    response_serializer=ar__condicionado__pb2.ar_condicionado_info.SerializeToString,
            ),
            'ar_condicionado_off': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_off,
                    request_deserializer=ar__condicionado__pb2.info_request.FromString,
                    response_serializer=ar__condicionado__pb2.ar_condicionado_info.SerializeToString,
            ),
            'ar_condicionado_status': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_status,
                    request_deserializer=ar__condicionado__pb2.info_request.FromString,
                    response_serializer=ar__condicionado__pb2.ar_condicionado_info.SerializeToString,
            ),
            'ar_condicionado_temp': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_temp,
                    request_deserializer=ar__condicionado__pb2.change_temp.FromString,
                    response_serializer=ar__condicionado__pb2.ar_condicionado_info.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ar_condicionado', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ar_condicionado(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ar_condicionado_on(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ar_condicionado/ar_condicionado_on',
            ar__condicionado__pb2.info_request.SerializeToString,
            ar__condicionado__pb2.ar_condicionado_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ar_condicionado_off(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ar_condicionado/ar_condicionado_off',
            ar__condicionado__pb2.info_request.SerializeToString,
            ar__condicionado__pb2.ar_condicionado_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ar_condicionado_status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ar_condicionado/ar_condicionado_status',
            ar__condicionado__pb2.info_request.SerializeToString,
            ar__condicionado__pb2.ar_condicionado_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ar_condicionado_temp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ar_condicionado/ar_condicionado_temp',
            ar__condicionado__pb2.change_temp.SerializeToString,
            ar__condicionado__pb2.ar_condicionado_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)