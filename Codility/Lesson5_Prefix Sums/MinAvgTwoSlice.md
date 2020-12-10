# MinAvgTwoSlice
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    min_num = sum(A[0:2])/2
    ans = 0
    if N == 2: return ans
    for i in range(3, N+1):
        avg = sum(A[i-2:i])/2
        if avg < min_num:
            ans = i-2
            min_num = avg
        avg = sum(A[i-3:i])/3
        if avg < min_num:
            ans = i-3
            min_num = avg
    return ans
```