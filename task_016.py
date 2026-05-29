x1, y1, w1, h1 = map(float, input().split())
x2, y2, w2, h2 = map(float, input().split())
x1_min, x1_max = x1, x1 + w1
y1_min, y1_max = y1, y1 + h1
x2_min, x2_max = x2, x2 + w2
y2_min, y2_max = y2, y2 + h2
inside_a = (x2_min <= x1_min and x1_max <= x2_max and y2_min <= y1_min and y1_max <= y2_max)
inside_b = (x1_min <= x2_min and x2_max <= x1_max and y1_min <= y2_min and y2_max <= y1_max)
intersect = (max(x1_min, x2_min) <= min(x1_max, x2_max) and max(y1_min, y2_min) <= min(y1_max, y2_max))
print(inside_a)
print(inside_a or inside_b)
print(intersect)
