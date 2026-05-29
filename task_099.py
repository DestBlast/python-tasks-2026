N = int(input())
lst = [int(input()) for _ in range(N)]
if N == 0:
    print(0)
else:
    max_len = 1
    curr_len = 1
    for i in range(1, N):
        if abs(lst[i] - lst[i-1]) == 1:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    print(max_len)