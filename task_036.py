N = int(input())
if N < 2:
    print("Нет")
else:
    is_prime = True
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            is_prime = False
            break
    print("Да" if is_prime else "Нет")