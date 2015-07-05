# coding=utf-8
__author__ = 'Jonater'

import os

dirname = os.path.dirname
join = os.path.join
sep = os.path.sep

ROOT_PATH = dirname(__file__)
PLUGINS_OPPOSITE_PATH = 'plugins'
PLUGINS_PATH = join(ROOT_PATH, PLUGINS_OPPOSITE_PATH)

WEAKPASS_DICT_PATH = join(ROOT_PATH, './data/weakpass_dict.txt')
PINYIN_PATH = join(ROOT_PATH, './data/pinyin_word.data')