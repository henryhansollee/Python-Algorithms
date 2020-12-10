# PermCheck
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # print(A)
    A = sorted(A)
    check = list(range(1, len(A)+1))
    # print(A)
    # print(check)
    if A == check: return 1
    else: return 0
```