lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
diff = []
i, j = 0, 0
while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        diff.append(lst1[i])
        i += 1
    elif lst1[i] > lst2[j]:
        j += 1
    else:
        i += 1
        j += 1
while i < len(lst1):
    diff.append(lst1[i])
    i += 1
print(*diff)