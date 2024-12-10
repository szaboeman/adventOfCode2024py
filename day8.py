from itertools import combinations

input=[row.strip() for row in open("input/day8.txt").readlines()]


def getUnique():
    unique = {}
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if  char!=".":
                if char not in unique:
                    unique[char] = []
                unique[char].append((i, j))
    return unique
unique=getUnique()

def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def task1():
        
    chords=set()
    for e in unique:
        parok=list(combinations(unique[e], 2))
        for p in parok:
            (x1,y1),(x2,y2)=p
            vx=x2-x1
            vy=y2-y1
            if in_bounds(input,x1+vx,y1+vy) and input[x1+vx][y1+vy]!=e:
                chords.add((x1+vx,y1+vy))
            if in_bounds(input,x1-vx,y1-vy) and input[x1-vx][y1-vy]!=e:
                chords.add((x1-vx,y1-vy))
            if in_bounds(input,x2+vx,y2+vy) and input[x2+vx][y2+vy]!=e:
                chords.add((x2+vx,y2+vy))
            if in_bounds(input,x2-vx,y2-vy) and input[x2-vx][y2-vy]!=e:
                chords.add((x2-vx,y2-vy))
    return len(chords)

print(task1())

def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def task2():
    chords=set()
    for e in unique:
        parok=list(combinations(unique[e], 2))
        for p in parok:
            (x1,y1),(x2,y2)=p
            vx=x2-x1
            vy=y2-y1
            ind=1
            while in_bounds(input,x1+vx*ind,y1+vy*ind) :
                if (input[x1+vx*ind][y1+vy*ind]!=e):
                    chords.add((x1+vx*ind,y1+vy*ind))
                ind+=1
            ind=1
            while in_bounds(input,x1-vx*ind,y1-vy*ind):
                if (input[x1-vx*ind][y1-vy*ind]!=e):
                    chords.add((x1-vx*ind,y1-vy*ind))
                ind+=1

    db=0
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if ((i,j)) in chords:
                db+=1
            elif(char!="."):
                db+=1
    return db
print(task2())