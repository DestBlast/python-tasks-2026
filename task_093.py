lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
common = []
i, j = 0, 0
while i < len(lst1) and j < len(lst2):
    if lst1[i] == lst2[j]:
        common.append(lst1[i])
        i += 1
        j += 1
    elif lst1[i] < lst2[j]:
        i += 1
    else:
        j += 1
print(*common)