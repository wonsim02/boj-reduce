from functools import reduce
from sys import stdin, stdout
from math import inf
stdout.write("%d %d\n" % (
    (lambda x: reduce(
        lambda y, z: (min(y[0], z), max(y[1], z)), x, (inf, -inf))
    )(map(int, stdin.read().splitlines()[1].split()))
))