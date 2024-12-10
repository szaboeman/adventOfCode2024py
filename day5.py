import math
from itertools import combinations

input="".join(open("input/day5.txt").readlines())

parts = input.strip().split("\n\n")

orderinRules=[list(map(int,line.split("|"))) for line in parts[0].splitlines()]
pagesToProduce=[list(map(int,line.split(","))) for line in parts[1].splitlines()]

def isGood(a, b):
    return [a,b] in orderinRules or not [b,a] in orderinRules 

def isAllGood(p):
     return all(isGood(x, y) for x, y in combinations(p, 2))

wrongOrder=[]

def task1():
    sum=0
    for pages in pagesToProduce:
        if isAllGood(pages):
            sum+=pages[int(math.floor(len(pages)/2))]
        else:
            wrongOrder.append(pages)
    return sum

print(task1())

def isAllGood(item, arr):
    return all(item == x or isGood(item, x) for x in arr)

def task2():
    sum=0
    for wrong in wrongOrder:
        goodOrdering=[]
        while wrong:
            i = next(i for i in range(len(wrong)) if isAllGood(wrong[i], wrong))
            goodOrdering.append(wrong.pop(i))
        sum+=goodOrdering[int(math.floor(len(goodOrdering)/2))]
    return sum
print(task2())
