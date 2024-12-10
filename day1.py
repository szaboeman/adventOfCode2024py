rows=open("input/day1.txt", 'r', encoding='utf-8').readlines()
left=sorted(int(data.strip().split('   ')[0]) for data in rows)
right=sorted(int(data.strip().split('   ')[1]) for data in rows)

print(left,right)
print(sum(abs(l - r) for l, r in zip(left, right)))
print(sum(l*right.count(l) for l in left))