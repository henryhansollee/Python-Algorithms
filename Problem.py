import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    nums = sorted(list(map(int, input().split())))
    ans = sum(nums[1:-1])
    print("#{} {}".format(tc, round(ans/len(nums[1:-1]))))