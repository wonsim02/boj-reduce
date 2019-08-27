from functools import reduce
gcd = lambda a, b: gcd(b, a%b) if a%b!=0 else b if b>0 else -b
n, ini = int(input()), int(input())
m = reduce(gcd, [int(input())-ini for i in range(n-1)])
l1, l2 = [], [m]
for i in range(2, m//2+1):
    if i*i > m:
        break
    elif i*i == m:
        l1.append(i)
    elif m%i == 0:
        l1.append(i)
        l2.insert(0, m//i)
print(" ".join(map(str, l1+l2)))