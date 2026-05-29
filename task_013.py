h = int(input())
m = int(input())
s = int(input())
total_hours = (h % 12) + m / 60 + s / 3600
angle = total_hours * 30
print(angle)
