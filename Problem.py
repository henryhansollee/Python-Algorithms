import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    nums = list(map(int, input().split()))
    ans = max(nums)
    print("#{} {}".format(tc, ans))