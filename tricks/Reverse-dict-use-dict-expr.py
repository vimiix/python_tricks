# coding: utf-8

d = {'a':1, 'b':2, 'c':3, 'd':4}
print(d.items())
# [('a', 1), ('c', 3), ('b', 2), ('d', 4)]

rd = {v:k for k,v in d.items()}
print(rd)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}