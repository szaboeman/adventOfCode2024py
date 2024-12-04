from collections import *

ALL_DIRS = [(-1, 0), (-1, -1), (1, 0), (-1, 1), (0, -1), (1, -1), (0, 1), (1, 1)]

def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])-1

input=open("input/day4.txt").readlines()
ALL_DIRS = [(-1, 0), (-1, -1), (1, 0), (-1, 1), (0, -1), (1, -1), (0, 1), (1, 1)]

db=0
for i in range(len(input)):
    for j in range(len(input[i])):
        for dir in ALL_DIRS:
            x=""
            for k in range(4):
                if in_bounds(input, i+dir[0]*k, j+dir[1]*k):
                    x+=input[i+dir[0]*k][j+dir[1]*k]
            if (x=="XMAS"):
                db+=1
print(db)


xMas=["MSAMS","MMASS","SMASM" ,"SSAMM"]
db=0
for i in range(len(input)):
    for j in range(len(input[i])):
        x=""
        for k in range(3):
            for l in range(3):
                if in_bounds(input, i+k, j+l):
                    if ((l+k)%2==0 or k==l):
                        x+=input[i+k][j+l]
        if (x in xMas):
            db+=1
print(db)