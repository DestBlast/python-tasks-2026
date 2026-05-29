N = int(input())
lst = [int(input()) for _ in range(N)]
left = 0
while left < N - 1 and lst[left] <= lst[left + 1]:
    left += 1
if left == N - 1:
    print(0)
else:
    right = N - 1
    while right > 0 and lst[right - 1] <= lst[right]:
        right -= 1
    min_rem = min(N - 1 - left, right)
    i = 0
    j = right
    while i <= left and j < N:
        if lst[i] <= lst[j]:
            min_rem = min(min_rem, j - i - 1)
            i += 1
        else:
            j += 1
    print(min_rem)