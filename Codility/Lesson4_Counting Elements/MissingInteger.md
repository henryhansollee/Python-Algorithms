# MissingInteger
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    check = [0] * 1000000
    for i in A:
        if i > 0 and check[i-1] == 0:
            check[i-1] += 1
    for i in range(len(check)):
        if check[i] == 0:
            return i+1
```