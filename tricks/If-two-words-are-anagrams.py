# coding: utf-8
# 检查两个字符串是否包含相同个数的字符组成

from collections import Counter
def is_anagram(str1, str2):
     return Counter(str1) == Counter(str2)

res = is_anagram('abcd', 'dbca')
print(res)
# True

res = is_anagram('abcd', 'dbaa')
print(res)
# False