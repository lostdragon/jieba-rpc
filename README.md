jieba-rpc
=============
[![Build Status](https://travis-ci.org/lostdragon/jieba-rpc.svg?branch=master)](https://travis-ci.org/lostdragon/jieba-rpc)

Simple [jieba](https://github.com/fxsjy/jieba) RPC server based on [zerorpc](https://github.com/0rpc/zerorpc-python).


## Installation

Install `jieba-rpc`:

```bash
python setup.py install
```


## Usage

You can start a simple jieba RPC server by executing:

```bash
python -m jiebarpc tcp://127.0.0.1:8888
```

Or if you wish to customize it using codes:

```python
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
        print('Usage: %s tcp://host:port' % sys.argv[0])
        sys.exit(1)

    endpoint = sys.argv[1]
    sys.exit(main(endpoint))
```


## License

The MIT License (MIT)

Copyright (c) 2014 messense

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
