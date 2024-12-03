import re

mul=r"mul\((\d+),(\d+)\)"
do=r"^.*?(?=do\(\))"
dont=r"don't\(\)"

input=open("input/day3.txt").readlines()
print(sum(sum(int(x)*int(y) for x,y in re.findall(mul, row)) for row in input))

matches = re.split(dont, "do()"+"".join(input))
print(sum(sum(int(x)*int(y) for x,y in re.findall(mul, re.sub(do, '', matches[i]))) for i in range(len(matches)) if "do()" in matches[i] or i==0))
