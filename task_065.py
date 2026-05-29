N = int(input())
lst = [int(input()) for _ in range(N)]
counts = {}
for x in lst:
    counts[x] = counts.get(x, 0) + 1
seen = set()
unique = []
repeated = []
for x in lst:
    if x not in seen:
        seen.add(x)
        if counts[x] == 1:
            unique.append(x)
        else:
            repeated.append(x)
result = unique + repeated
print(*result)