import sys

def solution(array, length):
    start_index = 0
    max_sum = sum(array[start_index: start_index + length])
    moving_sum = max_sum
    while (start_index + length) < len(array):
        temp_sum = moving_sum + array[start_index + length] - array[start_index]
        if temp_sum > max_sum:
            max_sum = temp_sum
        moving_sum = temp_sum
        start_index += 1
    return max_sum

array_length, num_length = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
answer = solution(array, num_length)
print(answer)