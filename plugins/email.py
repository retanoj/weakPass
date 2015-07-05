# coding=utf-8
__author__ = 'Jonater'

rules = [
    lambda x: x.split('@')[0]
]

def generator(data):
    if not data: return []

    result = []
    for _ in rules:
        result.extend(map(_, data))
    return list(set(result))
