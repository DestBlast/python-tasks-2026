x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
x4, y4 = map(float, input().split())
s1 = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
s2 = 0.5 * abs(x1 * (y3 - y4) + x3 * (y4 - y1) + x4 * (y1 - y3))
total_area = s1 + s2
print(total_area)
