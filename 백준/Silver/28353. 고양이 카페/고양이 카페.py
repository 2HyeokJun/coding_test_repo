import sys



def solution(n, k, array):
    answer = 0
    array.sort()
    start_index = 0
    end_index = n -1

    while start_index < end_index:
        sum = array[start_index] + array[end_index]
        if sum <= k:
            answer += 1
            start_index += 1
            end_index -= 1
        else:
            end_index -= 1

    return answer



n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
answer = solution(n, k, array)
print(answer)
