import sys

def solution(array_length, array, target):
    filtered = list(filter(lambda x: x <= target, array))
    filtered.sort()
    start_index = 0
    last_index = len(filtered) - 1
    answer = 0

    while start_index < last_index:
        start = filtered[start_index]
        end = filtered[last_index]
        sum = start + end
        if sum == target:
            answer += 1
            start_index += 1
            last_index -= 1
        elif sum > target:
            last_index -= 1
        else:
            start_index += 1
    return answer
    

array_length = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
answer = solution(array_length, array, target)
print(answer)