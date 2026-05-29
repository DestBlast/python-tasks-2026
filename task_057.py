N = int(input())
lst = [int(input()) for _ in range(N)]
found = False
for i in range(1, N - 1):
    if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
        print(lst[i])
        found = True
        break
if not found:
    print("no")