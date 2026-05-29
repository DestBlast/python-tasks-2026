N = int(input())
lst = [int(input()) for _ in range(N)]
total_sum = sum(lst)
left_sum = 0
possible = False
for i in range(N - 1):
    left_sum += lst[i]
    if left_sum == total_sum - left_sum:
        possible = True
        break
print("Да" if possible else "Нет")