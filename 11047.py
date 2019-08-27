from functools import reduce
n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
print(reduce(lambda x, y: (x[0]%y, x[1]+x[0]//y), reversed(c), (k, 0))[1])