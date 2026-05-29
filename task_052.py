N = int(input())
lst = [int(input()) for _ in range(N)]
count = 0
for i in range(1, N - 1):
    if lst[i] > lst[i - 1] and lst[i] < lst[i + 1]:
        count += 1
print(count)