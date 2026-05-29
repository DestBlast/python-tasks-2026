lst = list(map(int, input().split()))
count = sum(1 for x in lst if x % 2 == 0)
print(count)