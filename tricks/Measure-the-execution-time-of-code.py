# The "timeit" module lets you measure the execution
# time of small bits of Python code

import timeit

rt = timeit.timeit('"-".join(str(n) for n in range(100))',
                  number=10000)
print(rt)
# 0.252703905106

rt = timeit.timeit('"-".join([str(n) for n in range(100)])',
                  number=10000)
print(rt)
# 0.234980106354

rt = timeit.timeit('"-".join(map(str, range(100)))',
                  number=10000)
print(rt)
# 0.152318954468
