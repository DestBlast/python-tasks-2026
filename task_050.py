for num in range(10, 100):
    a = num // 10
    b = num % 10
    if (a + b) ** 2 == num:
        print(num)