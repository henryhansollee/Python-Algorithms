# CyclicRotation
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    # print(A, K)
    for i in range(K):
        # print(i)
        if len(A) > 1:
            A.insert(0, A.pop())
    # print(A)
    return A
```