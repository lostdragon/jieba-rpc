# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import zerorpc
from jiebarpc.dispatcher import JiebaRPCDispatcher


class JiebaRPCServer(zerorpc.Server):
    def __init__(self, methods=None, *args, **kwargs):
        methods = methods or JiebaRPCDispatcher()
        super(JiebaRPCServer, self).__init__(
            methods,
            *args,
            **kwargs
        )


if __name__ == '__main__':
    server = JiebaRPCServer()
    server.bind('tcp://0.0.0.0:4242')
    server.run()
