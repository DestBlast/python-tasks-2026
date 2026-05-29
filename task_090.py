N = int(input())
lst = [int(input()) for _ in range(N)]
result = []
for i in range(N):
    found = False
    for j in range(i + 1, N):
        if lst[j] == lst[i]:
            result.append(j - i)
            found = True
            break
    if not found:
        result.append(0)
print(result)