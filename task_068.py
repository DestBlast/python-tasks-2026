N = int(input())
lst = [int(input()) for _ in range(N)]
if not lst:
    print(0)
else:
    max_so_far = lst[0]
    curr_max = lst[0]
    for i in range(1, N):
        curr_max = max(lst[i], curr_max + lst[i])
        max_so_far = max(max_so_far, curr_max)
    print(max_so_far)