import sys
sys.stdin = open("Input.txt", "r")

P, K = map(int, input().split())
print(P-K+1)