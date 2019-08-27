from functools import reduce
t = int(input())
for i in range(t):
    k, n = int(input()), int(input())
    print(reduce(lambda x, y: x*y, range(n, n+k+1)) // 
          reduce(lambda x, y: x*y, range(1, k+2)))