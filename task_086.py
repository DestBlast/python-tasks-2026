N = int(input())
lst = [int(input()) for _ in range(N)]
inversions = 0
for i in range(N):
    for j in range(i + 1, N):
        if lst[i] > lst[j]:
            inversions += 1
print(inversions)