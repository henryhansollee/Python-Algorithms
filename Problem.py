import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    index = nums[-1]
    for i in range(n-1, -1, -1):
        if index > nums[i]:
            ans += (index - nums[i])
        else:
            index = nums[i]
    print("#{} {}".format(tc, ans))