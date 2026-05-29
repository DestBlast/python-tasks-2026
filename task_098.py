N = int(input())
lst = [int(input()) for _ in range(N)]
found = False
last_seen = {}
for i, x in enumerate(lst):
    if x in last_seen:
        prev_idx = last_seen[x]
        between = lst[prev_idx + 1 : i]
        if len(between) == len(set(between)):
            found = True
            break
    last_seen[x] = i
print("Да" if found else "Нет")