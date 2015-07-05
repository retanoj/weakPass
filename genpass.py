# coding=utf-8
__author__ = 'Jonater'

from itertools import permutations, product
from config import *

class genpass(object):
    def __init__(self):
        self.plugins = {}
        self.passwords = []

    def load_models(self, models):
        for plugin_name, plugin_model in models.iteritems():
            try:
                if not plugin_model['data']: continue
                _import_path = '.'.join(PLUGINS_OPPOSITE_PATH.split(sep))
                plugin_path = '%s.%s' % (_import_path, plugin_model['plugin'])
                _plugin = __import__(plugin_path, fromlist='*')
                self.plugins[plugin_name] = {}
                self.plugins[plugin_name]['name'] = plugin_name
                self.plugins[plugin_name]['handle'] = _plugin
                self.plugins[plugin_name]['data'] = plugin_model['data']
                print 'success load plugin <%s>.' % plugin_name
            except Exception:
                print 'error load plugin <%s>.' % plugin_name

    def generator_weakpass(self):
        combine_list = []

        for _, plugin in self.plugins.iteritems():
            model = plugin['handle']
            try:
                combine_list.append( model.generator(plugin['data']) )
            except Exception,e:
                print 'gen pwd from <%s> failed.' % plugin['name'], e

        pwds = []
        #for i in xrange(len(combine_list)):
        for i in xrange(3):
            for cl in permutations(combine_list, i+1):
                for pwd in product(*cl):
                    pwds.append(''.join(pwd))

        print 'generate weak passwords done.'
        self.passwords = list(set(pwds))
        return self.passwords

    def save_to_file(self, filename):
        with open(filename,'wb') as outf:
            for d in self.passwords:
                outf.write(d+'\n')
        print 'save to file <%s> done.' % filename
