# coding=utf-8
__author__ = 'Jonater'

import json
from genpass import genpass as gp
from config import *


def main():
    with open('config.json') as inf:
        models = json.loads(inf.read())
    if models and isinstance(models, dict):
        genpass = gp()

        for plugin_name, plugin_model in models.iteritems():
            try:
                _import_path = '.'.join(PLUGINS_OPPOSITE_PATH.split(sep))
                plugin_path = '%s.%s' % (_import_path, plugin_model['plugin'])
                _plugin = __import__(plugin_path, fromlist='*')
                genpass.plugins[plugin_name] = {}
                genpass.plugins[plugin_name]['name'] = plugin_name
                genpass.plugins[plugin_name]['handle'] = _plugin
                genpass.plugins[plugin_name]['data'] = plugin_model['data']
            except Exception:
                print 'error load plugin <%s>' % plugin_name

        passwords = genpass.generator_weakpass()
        save_to_file(passwords)

def save_to_file(data):
    with open("result.txt",'wb') as outf:
        for d in data:
            outf.write(d+'\n')

if __name__ == '__main__':
    main()