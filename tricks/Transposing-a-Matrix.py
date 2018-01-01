# Transposing a Matrix

mat = [[1, 2, 3], [4, 5, 6]]
res = zip(*mat)
print(res)
# [(1, 4), (2, 5), (3, 6)]