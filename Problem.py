import sys
sys.stdin = open("Input.txt", "r")

A, B = map(int, input().split())
ans = ''
if A == 1 and B == 2:
    ans = 'B'
elif A == 1 and B == 3:
    ans = 'A'
elif A == 2 and B == 1:
    ans = 'A'
elif A == 2 and B == 3:
    ans = 'B'
elif A == 3 and B == 1:
    ans = 'B'
elif A == 3 and B == 2:
    ans = 'A'
print(ans)