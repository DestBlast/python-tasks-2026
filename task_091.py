N = int(input())
lst = [int(input()) for _ in range(N)]
counts = {}
for x in lst:
    counts[x] = counts.get(x, 0) + 1
max_count = max(counts.values())
for x in lst:
    if counts[x] == max_count:
        print(f"{x} {max_count}")
        break