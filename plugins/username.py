# coding=utf-8
__author__ = 'Jonater'

rules = [
    #lambda x: x.title(),
    #lambda x: x.upper(),
    lambda x: x,
]

def generator(data):
    if not data: return []

    result = []
    for _ in rules:
        result.extend(map(_, data))
    return list(set(result))