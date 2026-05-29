num = int(input())
max1 = -1
max2 = -1
while num > 0:
    digit = num % 10
    if digit > max1:
        max2 = max1
        max1 = digit
    elif digit > max2 and digit < max1:
        max2 = digit
    num //= 10
if max2 == -1:
    print("no")
else:
    print(max2)