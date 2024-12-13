from collections import Counter

def blinking(stone_counts):
    counts = Counter()

    for stone, n in stone_counts.items():
        if stone == 0:
            counts[1] += n
        elif len(str(stone)) % 2 == 0:
            stoneStr = str(stone)
            mid = len(stoneStr) // 2
            counts[int(stoneStr[:mid])] += n
            counts[int(stoneStr[mid:])] += n
        else:
            new_stone = stone * 2024
            counts[new_stone] += n
    a=input()
    print(counts)
    return counts

def task(start, times):
    stoneCounts = Counter(start)
    for _ in range(times):
        stoneCounts = blinking(stoneCounts)
    return stoneCounts

stones = [int(x) for x in "0 37551 469 63 1 791606 2065 9983586".split()]

print(sum(task(stones, 25).values()))
print(sum(task(stones, 75).values()))