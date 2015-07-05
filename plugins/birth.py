# coding=utf-8
__author__ = 'Jonater'

rules = [
    '%Y',
    '%m%d',
    '%Y%m%d',
    '%y%m%d',
]

def generator(data):
    if not data: return []

    import time
    try:
        data = map(lambda x: time.strptime(x, '%Y-%m-%d'), data)
    except Exception,e:
        print 'bith data format error'
        return []

    result = []
    for _ in rules:
        result.extend(map(lambda x: time.strftime(_, x), data))
    return list(set(result))
