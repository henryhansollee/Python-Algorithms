import sys
sys.stdin = open("Input.txt", "r")

num = input()
ans = 0
for i in range(len(num)):
    ans += int(num[i])
print(ans)