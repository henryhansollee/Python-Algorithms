import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    a, b = map(int, input().split())
    ans = ''
    if a > b:
        ans = '>'
    elif a < b:
        ans = '<'
    else:
        ans = '='
    print("#{} {}".format(tc, ans))