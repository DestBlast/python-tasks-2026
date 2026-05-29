num = int(input())
counts = [0] * 10
temp = num
while temp > 0:
    counts[temp % 10] += 1
    temp //= 10
found = False
for d in range(10):
    if counts[d] == 1:
        print(d)
        found = True
        break
if not found:
    print("нет")