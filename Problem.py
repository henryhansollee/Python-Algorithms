import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 2:
            ans += i
        else:
            ans -= i
    print("#{} {}".format(tc, ans))