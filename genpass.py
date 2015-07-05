# coding=utf-8
__author__ = 'Jonater'

from itertools import permutations, product

class genpass(object):
    def __init__(self):
        self.plugins = {}

    def generator_weakpass(self):
        combine_list = []

        for _, plugin in self.plugins.iteritems():
            model = plugin['handle']
            combine_list.append( model.generator(plugin['data']) )

        passwords = []
        #for i in xrange(len(combine_list)):
        for i in xrange(3):
            for cl in permutations(combine_list, i+1):
                for pwd in product(*cl):
                    passwords.append(''.join(pwd))

        return list(set(passwords))