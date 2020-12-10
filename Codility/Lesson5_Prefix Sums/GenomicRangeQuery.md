# GenomicRangeQuery
```python
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    consistT = [[0]*(len(S)+1) for _ in range(4)]
    ans = []
    for i in range(len(S)):
        consistT[0][i+1] = consistT[0][i]
        consistT[1][i+1] = consistT[1][i]
        consistT[2][i+1] = consistT[2][i]
        consistT[3][i+1] = consistT[3][i]
        consistT[factor[S[i]]-1][i+1] += 1
        print(consistT)
    for i in range(len(P)):
        for j in range(4):
            if consistT[j][Q[i]+1] - consistT[j][P[i]] > 0:
                ans.append(j+1)
                break
    return ans
```