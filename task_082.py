N = int(input())
lst = [int(input()) for _ in range(N)]
total_sum = sum(lst)
if total_sum % 3 != 0:
    print("Нет")
else:
    target = total_sum // 3
    curr_sum = 0
    parts = 0
    for x in lst:
        curr_sum += x
        if curr_sum == target:
            parts += 1
            curr_sum = 0
    if parts >= 3:
        print("Да")
    else:
        print("Нет")