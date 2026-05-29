N = int(input())
lst = [int(input()) for _ in range(N)]
if len(set(lst)) == N - 1:
    print("Да")
else:
    print("Нет")