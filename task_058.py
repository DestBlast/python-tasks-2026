N = int(input())
lst = [int(input()) for _ in range(N)]
idx = -1
for i in range(1, N - 1):
    if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
        idx = i
if idx != -1:
    print(idx)
else:
    print("no")