N = int(input())
for i in range(1, N + 1):
    row = [str(i * j) for j in range(1, N + 1)]
    print(" ".join(row))