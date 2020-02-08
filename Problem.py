import sys
sys.stdin = open("Input.txt", "r")

words = input()
for word in words:
    print(word.upper(), end='')