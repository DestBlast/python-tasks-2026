N = int(input())
lst = [int(input()) for _ in range(N)]
seconds = set()
for i in range(N - 2):
    sub = sorted(lst[i:i+3])
    seconds.add(sub[1])
print(len(seconds))