# coding: utf-8

"""切片方式"""
a = [5, 4, 3, 2, 1]
print(a[::-1])

"""列表内建函数,会改变数组本身"""
a.reverse()
print(a)

a = [5, 4, 3, 2, 1]
"""函数方式, reversed()返回一个迭代器"""
print([i for i in reversed(a)])
