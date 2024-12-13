from collections import *

grid = [row.strip() for row in open("input/day12.txt").read().splitlines()]


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def neighbors4(grid, r, c):
    for dr, dc in DIRECTIONS:
        rr, cc = r + dr, c + dc
        if in_bounds(grid, rr, cc):
            yield (rr, cc)

def getPermiter(grid, start):
    c=0
    for dr, dc in DIRECTIONS:
        rr, cc = start[0] + dr, start[1] + dc
        if not in_bounds(grid, rr, cc) or in_bounds(grid, rr, cc) and grid[rr][cc]!=grid[start[0]][start[1]]:
            c+=1
    return c 


def CornersCount( cells):
    corners = 0
    for cell in cells:
        for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            if ((cell[0] + dx, cell[1]) not in cells and (cell[0], cell[1] + dy) not in cells):
                corners += 1
            if ((cell[0] + dx, cell[1]) in cells and (cell[0], cell[1] + dy) in cells and
                    (cell[0] + dx, cell[1] + dy) not in cells):
                corners += 1
    return corners

seen=set()

def bfs(start):
    cells=set()
    q = deque([start])
    cells.add(start)
    seen.add(start)
    permiter=0 # getPermiter(grid, start)
    terulet=0 # 1
    while q:
        pos = q.popleft()
        x,y=pos
        terulet+=1
        permiter+=getPermiter(grid,pos)
        for npos in neighbors4(grid, x,y):
            if npos not in seen:
                new_x,new_y=npos
                if grid[x][y]==grid[new_x][new_y]:
                    q.append(npos)
                    seen.add(npos)
                    cells.add(npos)
    return terulet,permiter, CornersCount(cells)

sum=0
sumb=0
for i, row in enumerate(grid):
    for j,value in enumerate(row):
        if (i,j) not in seen:
            t,k,s=bfs((i,j))
            print(value,t,s)
            sum+=t*k
            sumb+=t*s
print(sum)   
print(sumb)   
