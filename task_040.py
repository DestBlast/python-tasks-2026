N = int(input())
for i in range(N, 0, -1):
    row = "".join(str(j) for j in range(1, i + 1))
    print(row)