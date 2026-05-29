lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
union = []
i, j = 0, 0
def append_unique(val):
    if not union or union[-1] != val:
        union.append(val)
while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        append_unique(lst1[i])
        i += 1
    elif lst1[i] > lst2[j]:
        append_unique(lst2[j])
        j += 1
    else:
        append_unique(lst1[i])
        i += 1
        j += 1
while i < len(lst1):
    append_unique(lst1[i])
    i += 1
while j < len(lst2):
    append_unique(lst2[j])
    j += 1
print(*union)