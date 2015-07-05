# coding=utf-8
__author__ = 'Jonater'

import json
from genpass import genpass as gp
from config import flag

def main():
    with open('config.json') as inf:
        models = json.loads(inf.read())
    if models and isinstance(models, dict):
        genpass = gp()
        genpass.load_models(models)
        genpass.generator_weakpass()
        genpass.save_to_file('result.txt')

if __name__ == '__main__':
    print flag
    main()