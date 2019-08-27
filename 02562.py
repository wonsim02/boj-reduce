from functools import reduce
print("\n".join(map(str, (reduce(
    lambda x, y: (y, x[2], x[2]+1) if x[0]<y else (x[0], x[1], x[2]+1), 
    map(lambda x: int(input()), range(9)), (0, 0, 1)
))[:2])))