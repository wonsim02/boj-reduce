from functools import reduce
print(reduce(lambda x, y: "%d\n%d\n%d\n%d\n%d" % (x+y, x-y, x*y, x//y, x%y), map(int, input().split())))