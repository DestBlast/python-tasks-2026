N = int(input())
lst = [int(input()) for _ in range(N)]
if lst == lst[::-1]:
    print("Да")
else:
    print("Нет")