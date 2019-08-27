from functools import reduce
d = lambda n: (reduce(lambda x, y: (x[0]+x[1]%10, x[1]//10), range(4), (n, n)))[0]
print("\n".join(map(
    str, filter(
        lambda n: reduce(
            bool.__and__, map(
                n.__ne__, map(d, range(max(1, n-9*len(str(n))), n))
            ), True
        ), range(1, 10000)
    )
)))