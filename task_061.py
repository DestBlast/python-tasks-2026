N = int(input())
lst = [int(input()) for _ in range(N)]
def is_palindrome(l):
    return l == l[::-1]
if is_palindrome(lst):
    print("Да")
else:
    possible = False
    for i in range(N):
        if is_palindrome(lst[:i] + lst[i+1:]):
            possible = True
            break
    print("Да" if possible else "Нет")