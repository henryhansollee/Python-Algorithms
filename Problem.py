import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    a, b = map(int, input().split())
    print("#{} {} {}".format(tc, a // b, a % b))