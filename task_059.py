lst = list(map(int, input().split()))
if lst:
    max_val = max(lst)
    print(lst.index(max_val))