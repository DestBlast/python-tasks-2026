N = int(input())
evens = [str(i) for i in range(1, N + 1) if i % 2 == 0]
print(" ".join(evens))