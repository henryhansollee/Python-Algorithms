import sys
sys.stdin = open("Input.txt", "r")

t = int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())
    rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    temp = []
    for n in range(N):
        first, second, third = map(int, input().split())
        score = (first * 0.35) + (second * 0.45) + (third * 0.20)
        temp.append(score)
    index = N//10
    student = list(reversed(sorted(temp)))
    target = temp[K-1]
    target_index = student.index(target)
    for i in range(0, len(student), index):
        for j in range(i, i+index):
            student[j] = rank[i//index]
    print("#{} {}".format(tc, student[target_index]))