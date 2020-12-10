# CountDiv
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    # print(A, B, K)
    ans = B // K - A // K
    if A % K == 0:
        ans += 1
    return ans
```