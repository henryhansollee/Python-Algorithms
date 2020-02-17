import sys
sys.stdin = open("Input.txt", "r")

n = int(input())
for i in range(n+1):
    print(2 ** i, end=' ')