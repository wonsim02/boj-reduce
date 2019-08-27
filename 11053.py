from sys import stdin
from functools import reduce
seq = [int(n) for n in stdin.read().splitlines()[1].split()]
print(max(reduce(
    lambda x, y: (x[1].append(
        max([0]+[x[1][i] for i in range(y) if seq[i]<seq[y]])+1), 
                  x[1]), 
    range(1, len(seq)), [None, [1]])[1]))