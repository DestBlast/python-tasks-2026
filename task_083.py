N = int(input())
lst = [int(input()) for _ in range(N)]
min_len = float('inf')
for i in range(N):
    curr_sum = 0
    for j in range(i, N):
        curr_sum += lst[j]
        if curr_sum > 0:
            min_len = min(min_len, j - i + 1)
            break
if min_len == float('inf'):
    print("no")
else:
    print(min_len)