import sys



def solution(n, m, array):
    answer = 0
    array.sort()
    start_index = 0
    end_index = len(array) -1

    while start_index < end_index:
        sum = array[start_index] + array[end_index]
        if sum == m:
            answer += 1
            start_index += 1
            end_index -= 1
        elif sum < m:
            start_index += 1
        else:
            end_index -= 1

    return answer



n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))
answer = solution(n, m, array)
print(answer)