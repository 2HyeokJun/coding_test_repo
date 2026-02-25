import sys
import math


def _is_odd(number):
    return number % 2 != 0

def solution(n, array):
    array.sort()
    min_even_diff = math.inf
    min_odd_diff = math.inf
    odd_diff_array = []

    for i in range(n - 1):
        diff = abs(array[i+1] - array[i])
        if _is_odd(diff):
            min_odd_diff = min(min_odd_diff, diff)
            odd_diff_array.append(diff)
        else:
            min_even_diff = min(min_even_diff, diff)

    min_odd_diff = -1 if min_odd_diff == math.inf else min_odd_diff

    if min_even_diff != math.inf:
        return f"{min_even_diff} {min_odd_diff}"
    
    # 짝수차가 없을때 계산하는 로직
    
    if len(odd_diff_array) < 2:
        min_even_diff = -1
    else:
        min_odd_dif_sum = odd_diff_array[0] + odd_diff_array[1]
        for i in range(len(odd_diff_array) - 1):
            min_odd_dif_sum = min(min_odd_dif_sum, odd_diff_array[i] + odd_diff_array[i+1])
        min_even_diff = min_odd_dif_sum

    return f"{min_even_diff} {min_odd_diff}"

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))

answer = solution(n, array)
print(answer)