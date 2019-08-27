from sys import stdin
from functools import reduce
tri = map(lambda s: [int(c) for c in s.split()], stdin.read().splitlines()[1:])
print(max(reduce(lambda x, y: [x[0]+y[0]]+[max(x[i-1:i+1])+y[i] for i in range(1, len(y)-1)]+[x[-1]+y[-1]], tri)))