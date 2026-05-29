N = int(input())
lst = [int(input()) for _ in range(N)]
count = 0
for i in range(N - 1):
    if (lst[i] + lst[i+1]) % 2 == 0:
        count += 1
print(count)