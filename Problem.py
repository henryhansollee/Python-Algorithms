import sys
sys.stdin = open("Input.txt", "r")

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i
print(ans)