lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
merged = []
i, j = 0, 0
while i < len(lst1) and j < len(lst2):
    if lst1[i] <= lst2[j]:
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1
while i < len(lst1):
    merged.append(lst1[i])
    i += 1
while j < len(lst2):
    merged.append(lst2[j])
    j += 1
print(*merged)