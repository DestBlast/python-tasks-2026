N = int(input())
lst = [int(input()) for _ in range(N)]
counts = {}
for x in lst:
    counts[x] = counts.get(x, 0) + 1
unique_elements = [x for x in lst if counts[x] == 1]
if unique_elements:
    print(*(unique_elements))
else:
    print("no")