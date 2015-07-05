# coding=utf-8
__author__ = 'Jonater'

from lib.pinyin import PinYin
from config import PINYIN_PATH

rules = [
    lambda x: ''.join(x),
    lambda x: ' '.join(x).title().replace(' ', ''),
    lambda x: ''.join(map(lambda i: i[0], x)),
    lambda x: ''.join(map(lambda i: i[0], x)).title(),
    lambda x: ''.join(map(lambda i: i[0], x)).upper(),
    lambda x: '%s%s' % (x[0].title(), ''.join(map(lambda i: i[0], x[1:]))),
    lambda x: '%s%s' % (x[0], ''.join(map(lambda i: i[0], x[1:]))),
    lambda x: '%s%s' % (x[0].title(),''.join(x[1:])),
    #lambda x: ('%s%s' % (x[0], ''.join(map(lambda i: i[0], x[1:])))).upper(),
]

def generator(data):
    if not data: return []

    result = []
    py = PinYin(PINYIN_PATH)
    py.load_word()
    name_pinyin = map(py.hanzi2pinyin, data)
    for _ in rules:
        result.extend(map(_, name_pinyin))
    return list(set(result))
