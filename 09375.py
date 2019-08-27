from functools import reduce
t = int(input())
for i in range(t):
    clothes = {}
    n = int(input())
    for j in range(n):
        v, k = input().split()
        if k in clothes.keys():
            clothes[k] += 1
        else:
            clothes[k] = 1
    print(reduce(lambda x, y: x*(clothes[y]+1), clothes, 1)-1)