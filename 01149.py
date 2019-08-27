from sys import stdin
from functools import reduce
rgb = map(lambda x: [int(y) for y in x.split()], stdin.read().splitlines()[1:])
print(min(reduce(lambda a, b: (b[0]+min(a[1],a[2]), b[1]+min(a[2],a[0]), b[2]+min(a[0],a[1])), rgb, (0, 0, 0))))