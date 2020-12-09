import sys
sys.stdin = open("Input.txt", "r")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

N = 1041
def solution(N):
    # write your code in Python 3.6
    binary = bin(N)
    binary_num = binary[2:]
    print(binary)
    print(binary_num)
    one_index = []
    for index, value in enumerate(binary):
        if value == '1':
            one_index.append(index)
    print(one_index)

    binary_gap = []
    binary_gap.append(0)
    for idx in range(len(one_index)-1):
        binary_gap.append(one_index[idx+1] - one_index[idx] - 1)
    return max(binary_gap)
print(solution(N))
