#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from jiebarpc import JiebaRPCServer, JiebaRPCDispatcher


def main(endpoint):
    server = JiebaRPCServer(JiebaRPCDispatcher())
    server.bind(endpoint)
    server.run()
    return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: %s tcp://0.0.0.0:4242' % sys.argv[0])
        sys.exit(1)

    endpoint = sys.argv[1]
    sys.exit(main(endpoint))
