a = float(input())
b = float(input())
h = float(input())
projection = abs(a - b) / 2
side = (projection**2 + h**2) ** 0.5
perimeter = a + b + 2 * side
print(perimeter)