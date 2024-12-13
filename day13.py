import re

def getTokenNumber(x1, x2, y1, y2, v1, v2, taskB):
    if taskB:
        v1+=1e13
        v2+=1e13
    y=(v2*x1-v1*x2)/(x1*y2-y1*x2)
    x=(v1-y1*y)/x1
    if x % 1 == 0 and  y % 1 == 0:
        return int(x*3+y)
    else:
        return 0

with open('input/day13.txt') as f:
    lines = [list(map(int, re.findall(r'\d+', line))) for line in f.read().split("\n\n")]
    total_tokens, total_prices = 0, 0
    total_tokens_pt2, total_prices_pt2 = 0, 0
    token,tokenB=0,0
    for dx1, dy1, dx2, dy2, x, y in lines:
        token+=getTokenNumber(dx1, dy1, dx2, dy2, x, y,False)
        tokenB+=getTokenNumber(dx1, dy1, dx2, dy2, x, y,True)
    print(token)
    print(tokenB)

