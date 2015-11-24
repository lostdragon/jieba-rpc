# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import zerorpc
from jiebarpc.utils import ensure_unicode


class JiebaRPCClient(zerorpc.Client):
    @ensure_unicode
    def __call__(self, method, *args, **kargs):
        return super(JiebaRPCClient, self).__call__(method, *args)

    def cut(self, sentence, cut_all=False, HMM=True):
        return self.__call__(
            'cut',
            sentence,
            cut_all,
            HMM
        )

    def cut_for_search(self, sentence):
        return self.__call__(
            'cut_for_search',
            sentence
        )

    def extract_tags(self, sentence, topK=20, withWeight=False):
        return self.__call__(
            'extract_tags',
            sentence,
            topK,
            withWeight
        )

    def textrank(self, sentence, topK=10, withWeight=False):
        return self.__call__(
            'textrank',
            sentence,
            topK,
            withWeight
        )

    def posseg(self, sentence, HMM=True):
        return self.__call__(
            'posseg',
            sentence,
            HMM
        )

    def tokenize(self, sentence, mode='default', HMM=True):
        return self.__call__(
            'tokenize',
            sentence,
            mode,
            HMM
        )


if __name__ == '__main__':
    client = JiebaRPCClient("tcp://localhost:4242")
    print(client.cut('测试分词'))
    print(client.cut_for_search('测试分词'))
    print(client.extract_tags('测试分词'))
    print(client.textrank('测试分词'))
    print(client.tokenize('测试分词'))
    print(client.posseg('测试分词'))
