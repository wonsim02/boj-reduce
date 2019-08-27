from functools import reduce
A = int(input())
B = input()
S = map(lambda x: int(x)*A, B)
print("%s\n%d" % (reduce(lambda x, y: ("%d\n%s" % (y, x[0]) if type(x)!=int else "%d\n%d" % (y, x), 
                         x[1]*10+y if type(x)!=int else x*10+y), S)))