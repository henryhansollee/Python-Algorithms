# TapeEquilibrium
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # print(A)
    minA = 0
    maxA = sum(A)
    ans = 999999999
    for i in range(len(A)-1):
        minA += A[i]
        maxA -= A[i]
        ans = min(ans, abs(minA - maxA))
    return ans
```