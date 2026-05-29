num = int(input())
is_increasing = True
prev_digit = 10 
while num > 0:
    digit = num % 10
    if digit >= prev_digit:
        is_increasing = False
        break
    prev_digit = digit
    num //= 10
print("Да" if is_increasing else "Нет")