# coding: utf-8

d = {'a':1, 'b':2, 'c':3, 'd':4}
print(d.items())
# [('a', 1), ('c', 3), ('b', 2), ('d', 4)]

l = zip(d.values(), d.keys())
print(l)
# [(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]

rd = dict(l)
print(rd)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
