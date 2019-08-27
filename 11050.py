from functools import reduce
p = lambda n, m: reduce(lambda x, y: x*y, range(n, n-m, -1), 1)
print((lambda a: p(a[0], a[1])//p(a[1], a[1]))(list(map(int, input().split()))))