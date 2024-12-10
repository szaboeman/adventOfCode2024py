DIRECTIONS = [(-1, 0), (0, 1),(1, 0), (0, -1)]

input=open("input/day6.txt").readlines()
input = [sor.strip() for sor in input]
chords=set()

def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def startPos():
    for i,row in enumerate(input):
        for j,value in enumerate(row):
            if value!="#" and value!=".":
                return (i,j)

def task1():
    startx,starty=startPos()
    chords.add((startx,starty))
    dir=0
    while in_bounds(input,startx,starty):
        if (input[startx+DIRECTIONS[dir][0]][starty+DIRECTIONS[dir][1]]=="#"):
            dir=(dir+1)%4
        else:
            startx+=DIRECTIONS[dir][0]
            starty+=DIRECTIONS[dir][1]
            chords.add((startx,starty))
    return len(chords)-1

print(task1())


def getGoodChords():
    goodChords=[]
    for c in chords:
        for d in DIRECTIONS:
            if [c[0]+d[0],c[1]+d[1]] not in goodChords and input[c[0]+d[0]][c[1]+d[1]]==".":
                goodChords.append([c[0]+d[0],c[1]+d[1]])
    return goodChords

def hurok(input):
    startx,starty=startPos()
    chords=set()
    dir=0
    chords.add((startx,starty,dir))
    while in_bounds(input,startx,starty):
        if (in_bounds(input,startx+DIRECTIONS[dir][0],starty+DIRECTIONS[dir][1]) and 
            input[startx+DIRECTIONS[dir][0]][starty+DIRECTIONS[dir][1]]=="#"):
            dir=(dir+1)%4
        else:
            startx+=DIRECTIONS[dir][0]
            starty+=DIRECTIONS[dir][1]
            if (startx,starty,dir) not in chords:
                chords.add((startx,starty,dir))
            else:
                return True
    return False


good=set()
db=0

ind=0
for c in getGoodChords():
        x,y=startPos()
        ind+=1
        i,j=c
        if (in_bounds(input,i,j) and input[i][j]=="." and not(i==x and j==y) ):
            input[i]=input[i][:j]+"#" + input[i][j+1:]
            if hurok(input):
                good.add((i,j))
                db+=1
            input[i]=input[i][:j]+"." + input[i][j+1:]
print(db)