a = float(input())
b = float(input())
c = float(input())
x = float(input())
y = float(input())
brick = sorted([a, b, c])
hole = sorted([x, y])
if brick[0] <= hole[0] and brick[1] <= hole[1]:
    print("Пройдет")
else:
    print("Не пройдет")