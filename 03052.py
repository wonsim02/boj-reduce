from functools import reduce
from sys import stdin
print(sum((reduce(
    lambda x, y: (x[1].__setitem__(y%42, 1), x[1]) if x[1][y%42]==0 else x, 
    map(int, stdin.read().splitlines()), 
    (None, [0 for _ in range(42)])
))[1]))