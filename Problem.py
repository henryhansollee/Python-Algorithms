import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    words = input()
    ans = 999999999
    for i in range(len(words)):
        if words[:i] == words[i:i+i]:
            if i != 0:
                ans = min(ans, i)
    print("#{} {}".format(tc, ans))