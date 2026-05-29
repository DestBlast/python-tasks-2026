N = int(input())
lst = [int(input()) for _ in range(N)]
if not lst:
    print(0)
else:
    max_val = max(lst)
    first_idx = lst.index(max_val)
    last_idx = N - 1 - lst[::-1].index(max_val)
    if first_idx == last_idx:
        print(0)
    else:
        between_elements = lst[first_idx + 1 : last_idx]
        print(len(set(between_elements)))