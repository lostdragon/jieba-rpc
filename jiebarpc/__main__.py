#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import sys
import argparse
from jiebarpc import JiebaRPCServer, JiebaRPCDispatcher


def main(endpoint, processnum=1):
    server = JiebaRPCServer(JiebaRPCDispatcher(processnum))
    server.bind(endpoint)
    server.run()
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'python -m jiebarpc',
        description='Run jiebarpc server'
    )
    parser.add_argument('-n', '--processnum', type=int, default=1,
                        help='How many processes to use.')
    parser.add_argument('address',
                        help='Server listen address like tcp://127.0.0.1:8888', )
    ns = parser.parse_args()

    address = ns.address

    sys.exit(main(address, ns.processnum))
