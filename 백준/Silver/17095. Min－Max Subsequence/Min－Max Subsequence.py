import sys
import math
from copy import deepcopy


def solution(n, array):
    sorted_array = deepcopy(array)
    sorted_array.sort()

    min_element = sorted_array[0]
    max_element = sorted_array[n-1]

    min_index = None
    max_index = None
    answer = math.inf
    for i in range(n):
        element = array[i]
        if element == min_element:
            min_index = i
        if element == max_element:
            max_index = i
        if min_index is not None and max_index is not None:
            answer = min(answer, abs(min_index - max_index) + 1)
    return answer




    


n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))

answer = solution(n, array)
print(answer)