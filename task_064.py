N = int(input())
lst = [int(input()) for _ in range(N)]
seen = set()
result = []
for x in lst:
    if x not in seen:
        seen.add(x)
        result.append(x)
print(*result)