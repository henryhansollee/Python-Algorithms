import sys
sys.stdin = open("Input.txt", "r")

N = int(input())
nums = sorted(list(map(int, input().split())))
index = (N+1) // 2 - 1
ans = nums[index]
print(ans)