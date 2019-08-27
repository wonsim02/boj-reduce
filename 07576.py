from sys import stdin
from functools import reduce
from collections import deque
m, n = map(int, input().split())
tmt = [[int(y) for y in x.split()]+[-1] for x in stdin.read().splitlines()]
tmt.append([-1 for _ in range(m+1)])
day, cnt, queue = [[-1 for _ in range(m)] for _ in range(n)], 0, deque()
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(m):
        if tmt[i][j]==1:
            queue.append((i, j))
            day[i][j] = 0
while len(queue) > 0:
    i, j = queue.popleft()
    cnt = day[i][j]
    for dx, dy in dxdy:
        if tmt[i+dx][j+dy]==0:
            tmt[i+dx][j+dy] = 1
            day[i+dx][j+dy] = cnt+1
            queue.append((i+dx, j+dy))
print(cnt if reduce(int.__and__, map(lambda x: reduce(int.__and__, x), tmt)) else -1)