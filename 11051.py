from functools import reduce
PRIME = 10007
per_mod = lambda n, m: reduce(lambda x, y: x*y%PRIME, range(n, n-m, -1), 1)
inv_mod = lambda a, b: (1, 0) if a==1 else (lambda x: (x[1]-b//a*x[0], x[0]))(inv_mod(b%a, a))
print((lambda a: per_mod(a[0], a[1])*inv_mod(per_mod(a[1], a[1]), PRIME)[0]%PRIME) 
      (list(map(int, input().split()))))