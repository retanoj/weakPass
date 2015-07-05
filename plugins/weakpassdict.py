# coding=utf-8
__author__ = 'Jonater'

rules = [
    lambda x: x,
]

def generator(files):
    if not files: return []

    data = []
    for f in files:
        with open(f,'rb') as inf:
            data.extend(map(lambda x:x.strip(), inf.readlines()))

    result = []
    for _ in rules:
        result.extend(map(_, data))
    return list(set(result))