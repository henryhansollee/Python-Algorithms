import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    nums = list(map(int, input().split()))
    ans = 0
    for num in nums:
        if num % 2:
            ans += num
    print("#{} {}".format(tc, ans))