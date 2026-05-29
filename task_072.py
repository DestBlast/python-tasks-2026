N = int(input())
lst1 = [int(input()) for _ in range(N)]
lst2 = [int(input()) for _ in range(N)]
if len(lst1) != len(lst2):
    print("Нет")
else:
    double_lst1 = lst1 + lst1
    possible = False
    for i in range(N):
        if double_lst1[i:i+N] == lst2:
            possible = True
            break
    print("Да" if possible else "Нет")