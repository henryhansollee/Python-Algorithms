# FrogJmp
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    # print(X, Y, D)
    ans = (Y - X) / D
    temp = (Y - X) // D
    # print(ans)
    # print(temp)
    if ans > temp:
        return int(ans) + 1
    else:
        return int(ans)
```