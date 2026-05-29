N = int(input())
for _ in range(N):
    a = int(input())
    b = int(input())
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Равны")