# coding=utf-8
__author__ = 'Jonater'

import json
from genpass import genpass as gp
from config import flag

def main():
    try:
        models = {}
        with open('config.json') as inf:
            models = json.loads(inf.read())
    except Exception,e:
        print e

    if models and isinstance(models, dict):
        genpass = gp(models)
        genpass.generator_weakpass()
        genpass.save_to_file('result.txt')
    else:
        print 'load models error'

if __name__ == '__main__':
    print flag
    main()