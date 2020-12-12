# BinaryGap
```python
def solution(N):
    bin_num = bin(N)
    only_bin_num = bin_num[2:]
    index_list = []
    for index, value in enumerate(only_bin_num):
        if value == '1':
            index_list.append(index)
    ans = [0]
    for i in range(len(index_list)-1):
        ans.append(index_list[i+1] - index_list[i] - 1)
    return max(ans)
```