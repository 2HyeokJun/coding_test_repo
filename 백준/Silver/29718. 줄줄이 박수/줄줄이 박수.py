import sys

def sum_of_index(n, array, index):
    answer = 0
    for i in range(n):
        answer += array[i][index]
    return answer


def solution(n, m, array, a):
    max_clap = 0
    sum_of_clap = 0
    for i in range(m):
        sum_of_clap += sum_of_index(n, array, i)
        if (i + 1) - a > 0:
            sum_of_clap -= sum_of_index(n, array, i - a)
        max_clap = max(max_clap, sum_of_clap)
    return max(max_clap, sum_of_clap)

n, m = map(int, sys.stdin.readline().split())
array = []
for i in range(n):
    sub_array = list(map(int, sys.stdin.readline().split()))
    array.append(sub_array)
a = int(sys.stdin.readline().rstrip())

answer = solution(n, m, array, a)
print(answer)
