N = int(input())
lst = [int(input()) for _ in range(N)]
if N == 0:
    print(0)
else:
    max_len = 1
    cur_len = 1
    for i in range(1, N):
        if lst[i] == lst[i - 1]:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
    print(max_len)