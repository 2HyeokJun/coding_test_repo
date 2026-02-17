import sys


def solution(n, target, array):
    answer = 0
    for i in range(0, n):
        temp_sum = 0
        for j in range(i, n):
            temp_sum += array[j]
            if temp_sum == target:
                answer += 1
            elif temp_sum > target:
                break


    return answer

n, target = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
answer = solution(n, target, array)
print(answer)