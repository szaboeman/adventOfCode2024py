from collections import *

grid = open("input/day10.txt").read().splitlines()

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def neighbors4(grid, r, c):
    for dr, dc in DIRECTIONS:
        rr, cc = r + dr, c + dc
        if in_bounds(grid, rr, cc):
            yield (rr, cc)

def bfs(results,start,taskA, target=None):
    q = deque([(start, 0)])
    seen = {start}
    seen=set()
    if taskA: seen.add(start)
    while q:
        pos, value = q.popleft()
        x,y=pos
        if grid[x][y] ==target:
            results.append(pos)
        for npos in neighbors4(grid, *pos):
            if not taskA or npos not in seen:
                x,y=npos
                if grid[x][y]!='.' and int(grid[x][y])==int(value)+1:
                    if taskA: seen.add(npos)
                    q.append((npos, value + 1))


def getStartPosition():
    start=set()
    for i,row in enumerate(grid):
        for j, c in enumerate(row):
            if c=='0':
                start.add((i,j))
    return start


def task(taksA):
    results=list()
    for s in getStartPosition():
        bfs(results,s,taksA,'9')
        
    c=Counter(results)
    sum=0
    for key, value in c.items():
        sum+=value
    return sum


print(task(True))
print(task(False))