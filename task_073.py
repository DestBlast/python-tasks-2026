N = int(input())
lst1 = [int(input()) for _ in range(N)]
lst2 = [int(input()) for _ in range(N)]
shift = -1
for s in range(N):
    shifted = lst1[-s:] + lst1[:-s] if s > 0 else lst1
    if shifted == lst2:
        shift = s
        break
print(shift)