num = int(input())
max_len = 0
current_len = 0
prev_digit = -1
while num > 0:
    digit = num % 10
    if digit == prev_digit:
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
        current_len = 1
        prev_digit = digit
    num //= 10
if current_len > max_len:
    max_len = current_len
print(max_len)