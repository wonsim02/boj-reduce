from math import inf
from functools import reduce
c_div = lambda x, y: -(abs(x)//abs(y)) if x*y<0 else abs(x)//abs(y)
op_list = [int.__add__, int.__sub__, int.__mul__, c_div]
n, M, m = int(input()), -inf, inf
num = [int(x) for x in input().split()]
ops = [int(x) for x in input().split()]
used, stack = [0 for _ in range(4)], []
def f(i):
    if i==n-1:
        global M, m
        v = reduce(lambda x, y: op_list[stack[y]](x, num[y+1]), range(n-1), num[0])
        M, m = max(M, v), min(m, v)
        return
    for j in range(4):
        if used[j]<ops[j]:
            used[j] += 1
            stack.append(j)
            f(i+1)
            stack.pop()
            used[j] -= 1
f(0)
print("%d\n%d" % (M, m))