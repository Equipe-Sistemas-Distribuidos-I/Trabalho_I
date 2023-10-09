# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import devices_pb2 as devices__pb2


class ar_condicionadoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ar_condicionado_on = channel.unary_unary(
                '/ar_condicionado/ar_condicionado_on',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.ar_condicionado_info.FromString,
                )
        self.ar_condicionado_off = channel.unary_unary(
                '/ar_condicionado/ar_condicionado_off',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.ar_condicionado_info.FromString,
                )
        self.ar_condicionado_status = channel.unary_unary(
                '/ar_condicionado/ar_condicionado_status',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.ar_condicionado_info.FromString,
                )
        self.ar_condicionado_temp = channel.unary_unary(
                '/ar_condicionado/ar_condicionado_temp',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.ar_condicionado_info.FromString,
                )
        self.close_connection = channel.unary_unary(
                '/ar_condicionado/close_connection',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.ar_condicionado_info.FromString,
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

    def close_connection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ar_condicionadoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ar_condicionado_on': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_on,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.ar_condicionado_info.SerializeToString,
            ),
            'ar_condicionado_off': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_off,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.ar_condicionado_info.SerializeToString,
            ),
            'ar_condicionado_status': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_status,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.ar_condicionado_info.SerializeToString,
            ),
            'ar_condicionado_temp': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_temp,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.ar_condicionado_info.SerializeToString,
            ),
            'close_connection': grpc.unary_unary_rpc_method_handler(
                    servicer.close_connection,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.ar_condicionado_info.SerializeToString,
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
            devices__pb2.info_request.SerializeToString,
            devices__pb2.ar_condicionado_info.FromString,
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
            devices__pb2.info_request.SerializeToString,
            devices__pb2.ar_condicionado_info.FromString,
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
            devices__pb2.info_request.SerializeToString,
            devices__pb2.ar_condicionado_info.FromString,
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
            devices__pb2.info_request.SerializeToString,
            devices__pb2.ar_condicionado_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def close_connection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ar_condicionado/close_connection',
            devices__pb2.info_request.SerializeToString,
            devices__pb2.ar_condicionado_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class lampadaStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.lampada_on = channel.unary_unary(
                '/lampada/lampada_on',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.lampada_info.FromString,
                )
        self.lampada_off = channel.unary_unary(
                '/lampada/lampada_off',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.lampada_info.FromString,
                )
        self.lampada_status = channel.unary_unary(
                '/lampada/lampada_status',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.lampada_info.FromString,
                )


class lampadaServicer(object):
    """Missing associated documentation comment in .proto file."""

    def lampada_on(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def lampada_off(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def lampada_status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_lampadaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'lampada_on': grpc.unary_unary_rpc_method_handler(
                    servicer.lampada_on,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.lampada_info.SerializeToString,
            ),
            'lampada_off': grpc.unary_unary_rpc_method_handler(
                    servicer.lampada_off,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.lampada_info.SerializeToString,
            ),
            'lampada_status': grpc.unary_unary_rpc_method_handler(
                    servicer.lampada_status,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.lampada_info.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lampada', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class lampada(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def lampada_on(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lampada/lampada_on',
            devices__pb2.info_request.SerializeToString,
            devices__pb2.lampada_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def lampada_off(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lampada/lampada_off',
            devices__pb2.info_request.SerializeToString,
            devices__pb2.lampada_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def lampada_status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lampada/lampada_status',
            devices__pb2.info_request.SerializeToString,
            devices__pb2.lampada_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class geladeiraStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ar_condicionado_on = channel.unary_unary(
                '/geladeira/ar_condicionado_on',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.geladeira_info.FromString,
                )
        self.ar_condicionado_off = channel.unary_unary(
                '/geladeira/ar_condicionado_off',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.geladeira_info.FromString,
                )
        self.ar_condicionado_status = channel.unary_unary(
                '/geladeira/ar_condicionado_status',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.geladeira_info.FromString,
                )
        self.ar_condicionado_temp = channel.unary_unary(
                '/geladeira/ar_condicionado_temp',
                request_serializer=devices__pb2.change_temp.SerializeToString,
                response_deserializer=devices__pb2.geladeira_info.FromString,
                )


class geladeiraServicer(object):
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


def add_geladeiraServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ar_condicionado_on': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_on,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.geladeira_info.SerializeToString,
            ),
            'ar_condicionado_off': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_off,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.geladeira_info.SerializeToString,
            ),
            'ar_condicionado_status': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_status,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.geladeira_info.SerializeToString,
            ),
            'ar_condicionado_temp': grpc.unary_unary_rpc_method_handler(
                    servicer.ar_condicionado_temp,
                    request_deserializer=devices__pb2.change_temp.FromString,
                    response_serializer=devices__pb2.geladeira_info.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'geladeira', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class geladeira(object):
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
        return grpc.experimental.unary_unary(request, target, '/geladeira/ar_condicionado_on',
            devices__pb2.info_request.SerializeToString,
            devices__pb2.geladeira_info.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/geladeira/ar_condicionado_off',
            devices__pb2.info_request.SerializeToString,
            devices__pb2.geladeira_info.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/geladeira/ar_condicionado_status',
            devices__pb2.info_request.SerializeToString,
            devices__pb2.geladeira_info.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/geladeira/ar_condicionado_temp',
            devices__pb2.change_temp.SerializeToString,
            devices__pb2.geladeira_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class gateway_interfaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.use_device = channel.unary_unary(
                '/gateway_interface/use_device',
                request_serializer=devices__pb2.info_request.SerializeToString,
                response_deserializer=devices__pb2.geladeira_info.FromString,
                )


class gateway_interfaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def use_device(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_gateway_interfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'use_device': grpc.unary_unary_rpc_method_handler(
                    servicer.use_device,
                    request_deserializer=devices__pb2.info_request.FromString,
                    response_serializer=devices__pb2.geladeira_info.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gateway_interface', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class gateway_interface(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def use_device(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gateway_interface/use_device',
            devices__pb2.info_request.SerializeToString,
            devices__pb2.geladeira_info.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
