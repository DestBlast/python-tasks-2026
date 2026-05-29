N = int(input())
lst = [int(input()) for _ in range(N)]
max_so_far = -float('inf')
curr_max = 0
start = 0
end = 0
s = 0
for i in range(N):
    curr_max += lst[i]
    if max_so_far < curr_max:
        max_so_far = curr_max
        start = s
        end = i
    if curr_max < 0:
        curr_max = 0
        s = i + 1
print(start, end)