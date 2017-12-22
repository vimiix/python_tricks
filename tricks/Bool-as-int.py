# coding: utf-8
'''
Bool值可以作为整型数值来使用
    True -> 1
    False -> 0

这个用法比较含蓄
'''

num = 3

# 算术运算
print(isinstance(num, int) + (num < 10))
# 2

# 作索引用
print(['奇数', '偶数'][num % 2 == 0])
# 奇数
