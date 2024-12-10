input=open("input/day9.txt").readlines()[0].strip()




def getData():
    d=[]
    for i,c in enumerate(input):
        if (i%2==0):
            d.append((int(c),i//2,True))  #darab value
        else:
            d.append((int(c),"",False))  #darab value, False = pont
    return d

d=getData()
def task1():
    firstIndex=0
    sum=0
    index=0
    while firstIndex<len(d):
        db, v, isv=d[firstIndex]
        if isv:
            for j in range(db):
                sum+=index*v
                index+=1
            firstIndex+=1
        else:
            dbe, _, _=d[firstIndex]
            j=0
            while j<dbe:
                while not(d[-1][2]):
                    d.pop()
                dbv, vv, _=d[-1]
                sum+=index*vv
                d[-1]=(dbv-1,vv,_)
                if dbv-1==0:
                    d.pop()
                index+=1
                j+=1
            firstIndex+=1
    return sum
print(task1())


d=getData()
def move():
    lastIndex=len(d)-1
    while lastIndex>=0:
        while not(d[-1*(len(d)-lastIndex)][2]):
            lastIndex-=1
        dbv,vv,_=d[lastIndex]
        firstIndex=0
        while firstIndex<lastIndex and not (d[firstIndex][2]==False and d[firstIndex][0]>=dbv):
            firstIndex+=1
        
        if firstIndex<lastIndex:
            d[firstIndex]=(d[firstIndex][0]-dbv,"",False)
            d[lastIndex]=(dbv,"",False)
            d.insert(firstIndex,(dbv,vv,True))
        lastIndex-=1

def task2():
    move()
    firstIndex=0
    sum=0
    index=0
    while firstIndex<len(d):
        db, v, isv=d[firstIndex]
        if isv:
            for _ in range(db):
                sum+=index*v
                index+=1
            firstIndex+=1
        else:
            index+=db
            firstIndex+=1
    return sum
print(task2())