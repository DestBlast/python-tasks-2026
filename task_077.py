N = int(input())
lst = [int(input()) for _ in range(N)]
max_len = 0
curr_len = 0
for x in lst:
    if x % 2 == 0:
        curr_len += 1
        max_len = max(max_len, curr_len)
    else:
        curr_len = 0
print(max_len)