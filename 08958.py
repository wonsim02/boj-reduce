from functools import reduce
print("\n".join(map(
    lambda z: str(reduce(
        lambda x, y: (x[0]+x[1], x[1]+1) if y=='O' else (x[0], 1),
        input(), (0, 1)
    )[0]), range(int(input()))
)))