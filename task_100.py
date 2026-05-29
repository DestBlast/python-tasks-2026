N = int(input())
lst = [int(input()) for _ in range(N)]
def is_stable(l):
    for i in range(1, len(l) - 1):
        if not (min(l[i-1], l[i+1]) <= l[i] <= max(l[i-1], l[i+1])):
            return False
    return True
if is_stable(lst):
    print("Да")
else:
    possible = False
    for i in range(N):
        if is_stable(lst[:i] + lst[i+1:]):
            possible = True
            break
    print("Да" if possible else "Нет")