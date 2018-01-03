# coding: utf-8
# Transposing a Matrix

mat = [[1, 2, 3], [4, 5, 6]]
res = zip(*mat)
print(res)
# 注意:在py2中会直接输出下面的结果
# 在Py3中res是一个生成器，需求迭代输出结果。
# [(1, 4), (2, 5), (3, 6)]

# for 循环处理方法
res = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print(res)
# [[1, 4], [2, 5], [3, 6]]