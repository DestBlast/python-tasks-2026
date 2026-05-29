N = int(input())
lst = [int(input()) for _ in range(N)]
counts = {}
for x in lst:
    counts[x] = counts.get(x, 0) + 1
max_freq = max(counts.values()) if counts else 0
if max_freq <= (N + 1) // 2:
    print("Да")
else:
    print("Нет")