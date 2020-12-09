# BinaryGap
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    # print(N)
    binary_num = bin(N)
    # print(binary_num, type(binary_num))
    ones = []
    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            ones.append(i)
    # print(ones)
    gaps = []
    for i in range(len(ones)-1):
        gaps.append(ones[i+1] - ones[i] - 1)
    # print(gaps)
    if gaps:
        return max(gaps)
    else:
        return 0
```