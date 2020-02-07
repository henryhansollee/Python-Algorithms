import sys
sys.stdin = open("Input.txt", "r")

words = input()
for word in words:
    print(ord(word)-64, end=' ')