import sys
sys.stdin = open("Input.txt", "r")

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)