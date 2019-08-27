from functools import reduce
p = []

def get_prime_list(k):
    l = [2]
    for i in range(3, k+1, 2):
        is_prime = True
        for p in l[1:]:
            if i%p == 0:
                is_prime = False
        if is_prime:
            l.append(i)
    return l

def factorize(k):
    l, i, m = [0, 0, 0], 0, k
    while m!=1:
        if m%p[i]==0:
            l[i] += 1
            m //= p[i]
        else:
            i += 1
            l.append(0)
    return l

def euler(l, k):
    return reduce(lambda x, y: 
                  x*(p[y]-1)//p[y], 
                  filter(lambda z: l[z]>0, range(len(l))), k)

a, b, n = map(int, input().split())
p = get_prime_list(b)
e = factorize(b)
zero = max(e[0], e[2])
adjust = 2**(zero-e[0])*5**(zero-e[2])
c, d, e[0], e[2] = a*adjust, b*adjust//(10**zero), 0, 0
rotate, idx = 1 if d==1 else euler(e, d), zero-n
outer = ("%%0%dd" % zero) % (c//d)
inner = "0" if d==1 else ("%%0%dd" % rotate) % ((c%d)*(10**rotate-1)//d)
print(inner[(-idx-1)%rotate] if idx<0 else outer[-idx-1])
