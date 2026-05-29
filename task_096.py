N = int(input())
lst = [int(input()) for _ in range(N)]
required_unique = len(set(lst))
counts = {}
left = 0
min_len = float('inf')
unique_in_window = 0
for right in range(N):
    x = lst[right]
    if counts.get(x, 0) == 0:
        unique_in_window += 1
    counts[x] = counts.get(x, 0) + 1
    while unique_in_window == required_unique:
        min_len = min(min_len, right - left + 1)
        left_item = lst[left]
        counts[left_item] -= 1
        if counts[left_item] == 0:
            unique_in_window -= 1
        left += 1
print(min_len)