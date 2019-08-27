from functools import reduce
print((lambda x: x if x<=2 else reduce(lambda y, z: (y[1], sum(y)%15746), range(x-3), (2,3))[1])(int(input())))