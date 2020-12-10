# MaxCounters
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    ans = [0] * N
    curr_num = 0
    max_num = 0
    next_max_num = 0
    for i in range(len(A)):
        if 1 <= A[i] <= N:
            curr_num = max(ans[A[i]-1] + 1, max_num + 1)
            ans[A[i]-1] = curr_num
            next_max_num = max(curr_num, next_max_num)
        else:
            max_num = next_max_num
        # print(ans)
    return [x if x > max_num else max_num for x in ans]
```