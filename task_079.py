N = int(input())
lst = [int(input()) for _ in range(N)]
running_sum = 0
found = False
for i in range(N):
    if i > 0 and lst[i] == running_sum:
        found = True
        break
    running_sum += lst[i]
print("Да" if found else "Нет")