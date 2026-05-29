N = int(input())
lst = [int(input()) for _ in range(N)]
counts = {}
for x in lst:
    counts[x] = counts.get(x, 0) + 1
max_count = -1
best_element = None
for x in lst:
    if counts[x] > max_count:
        max_count = counts[x]
        best_element = x
print(best_element)