N = int(input())
lst = [int(input()) for _ in range(N)]
found = False
for i in range(N):
    current_sum = lst[i]
    for j in range(i + 1, N):
        current_sum += lst[j]
        if current_sum == 0:
            found = True
            break
    if found:
        break
print("Да" if found else "Нет")