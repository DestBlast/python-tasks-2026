N = int(input())
lst = [int(input()) for _ in range(N)]
pref_max = [-float('inf')] * N
suff_max = [-float('inf')] * N
curr = -float('inf')
for i in range(N):
    pref_max[i] = curr
    curr = max(curr, lst[i])
curr = -float('inf')
for i in range(N - 1, -1, -1):
    suff_max[i] = curr
    curr = max(curr, lst[i])
possible_maxes = set()
for i in range(N):
    val = max(pref_max[i], suff_max[i])
    if val != -float('inf'):
        possible_maxes.add(val)
print(*sorted(list(possible_maxes)))