# coding=utf-8
__author__ = 'Jonater'

import os

flag = r'''
                               _    ______
                              | |   | ___ \
        __      __ ___   __ _ | | __| |_/ /__ _  ___  ___
        \ \ /\ / // _ \ / _` || |/ /|  __// _` |/ __|/ __|
         \ V  V /|  __/| (_| ||   < | |  | (_| |\__ \\__ \
          \_/\_/  \___| \__,_||_|\_\\_|   \__,_||___/|___/

                    weak password generator
                                    --by retanoj(@Jonater)
'''

dirname = os.path.dirname
join = os.path.join
sep = os.path.sep

ROOT_PATH = dirname(__file__)
PLUGINS_OPPOSITE_PATH = 'plugins'
PLUGINS_PATH = join(ROOT_PATH, PLUGINS_OPPOSITE_PATH)

PINYIN_PATH = join(ROOT_PATH, './data/pinyin_word.data')