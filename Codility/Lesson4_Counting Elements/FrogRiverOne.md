# FrogRiverOne
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    check = [0] * X
    ans = 0
    for i in range(len(A)):
        if check[A[i]-1] == 0:
            check[A[i]-1] = 1
            ans += 1
            if ans == X:
                return i
    return -1
```