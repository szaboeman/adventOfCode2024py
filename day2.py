grid = [list(map(int,l.split(" "))) for l in open("input/day2.txt").read().splitlines()]

def isSafe(row):
    return (all(b - a < 4 and b-a>0 for a, b in zip(row, row[1:])) or 
            all(a - b < 4 and a-b>0 for a, b in zip(row, row[1:])))

print(sum(1 for row in grid if isSafe(row)))      
print(sum(1 for row in grid if any(isSafe(row[:i] + row[i+1:]) for i in range(len(row)))))
