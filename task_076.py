N = int(input())
lst = [int(input()) for _ in range(N)]
seen = set()
left = 0
max_len = 0
for right in range(N):
    while lst[right] in seen:
        seen.remove(lst[left])
        left += 1
    seen.add(lst[right])
    max_len = max(max_len, right - left + 1)
print(max_len)