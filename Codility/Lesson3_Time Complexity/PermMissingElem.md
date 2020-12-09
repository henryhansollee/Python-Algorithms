# PermMissingElem
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # print(A)
    N = len(A)
    target = N+1
    B = list(range(1, target+1))
    sumA = sum(A)
    sumB = sum(B)
    # print(sumA)
    # print(sumB)
    return sumB - sumA
```