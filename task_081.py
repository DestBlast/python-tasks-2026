N = int(input())
lst = [int(input()) for _ in range(N)]
count = 0
for i in range(N - 2):
    if lst[i+1] > lst[i] and lst[i+1] > lst[i+2]:
        count += 1
print(count)