import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    word = list(input())
    ans = 0
    if word == list(reversed(word)):
        ans = 1
    print("#{} {}".format(tc, ans))