N = int(input())
lst = [int(input()) for _ in range(N)]
total_sum = sum(lst)
left_sum = 0
ways = 0
for i in range(N - 1):
    left_sum += lst[i]
    if left_sum == total_sum - left_sum:
        ways += 1
print(ways)