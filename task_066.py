N = int(input())
lst = [int(input()) for _ in range(N)]
prefix_sums = {0: -1}
current_sum = 0
max_len = 0
for i in range(N):
    current_sum += lst[i]
    if current_sum in prefix_sums:
        length = i - prefix_sums[current_sum]
        if length > max_len:
            max_len = length
    else:
        prefix_sums[current_sum] = i
print(max_len)