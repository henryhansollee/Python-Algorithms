# PassingCars
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    ans = 0
    cnt = 0
    for i in range(len(A)):
        if A[i] and cnt == 0: continue
        elif not A[i]:
            cnt += 1
        elif A[i]:
            ans += cnt
    if ans > 1000000000:
        return -1
    return ans
```