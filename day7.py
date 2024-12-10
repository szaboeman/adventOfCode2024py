import re

input=open("input/day7.txt").readlines()
data=[]

for row in input:
    testValue,values=re.split(r": ",row.strip())
    testValue=int(testValue)
    values=[int(v) for v in values.strip().split(" ")]
    data.append([testValue,values])


def task(base,values,test):

    for num in range(base**(len(values)-1)):
        trinary = ""
        temp = num
        for _ in range(len(values)-1):
            trinary = str(temp % base) + trinary
            temp //= base
        trinary = trinary.zfill(len(values)-1)
        v=values[0]
        for i in range(len(values)-1):
            if trinary[i]=="0":
                v+=values[i+1]
            elif (trinary[i]=="1"):
                v*=values[i+1]
            else:
                v=int(str(v)+str(values[i+1]))
            if v>test:
                break
        if v==test:
            return True
    return False

print(sum(d[0] for d in data if task(2,d[1],d[0])))
print(sum(d[0] for d in data if task(3,d[1],d[0])))