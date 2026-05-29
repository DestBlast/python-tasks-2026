num = int(input())
for d in range(10):
    count = 0
    temp = num
    while temp > 0:
        if temp % 10 == d:
            count += 1
        temp //= 10
    print(f"{d}: {count}")