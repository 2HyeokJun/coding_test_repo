import sys

def print_answer(tuple):
    max = tuple[0]
    period = tuple[1]

    if max == 0:
        print("SAD")
    else:
        print(max)
        print(period)


def solution(n, x, array):
    period = 0

    # default settings
    max_sum = 0
    for i in range(0, x):
        max_sum += array[i]
    if max_sum > 0:
        period += 1

    index = 0
    temp_sum = max_sum
    for i in range(x, len(array)):
        temp_sum += array[i] - array[index]
        if temp_sum == max_sum:
            period += 1
        elif temp_sum > max_sum:
            period = 1
            max_sum = temp_sum
        index += 1
        
    return max_sum, period

n, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
answer = solution(n, x, array)
print_answer(answer)