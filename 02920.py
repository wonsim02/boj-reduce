from functools import reduce
print(["", "ascending", "descending", "mixed"][
    (lambda x: x[1]*2+x[0])(
        (lambda s: reduce(
            lambda x, y : (x[0] or x[2]<y, x[1] or x[2]>y, y), 
            s[1:], (False, False, s[0])
        ))([int(c) for c in input().split()])
    )
])