N = int(input())
lst = [int(input()) for _ in range(N)]
sorted_lst = sorted(lst)
is_strictly_increasing = all(sorted_lst[i] < sorted_lst[i+1] for i in range(N - 1))
if not is_strictly_increasing:
    print("Нет")
else:
    mismatches = [i for i in range(N) if lst[i] != sorted_lst[i]]
    if len(mismatches) == 2:
        print("Да")
    else:
        print("Нет")