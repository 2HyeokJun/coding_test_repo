import sys
from collections import deque


def solution(n, array):
    MAX_DIFF = 2
    max_length = 1


    start_index = 0 # 반석의 시작 index

    min_deque = deque()
    max_deque = deque()
    
    for i in range(n):
        while min_deque and array[min_deque[-1]] >= array[i]:
            min_deque.pop()
        min_deque.append(i)
        
        while max_deque and array[max_deque[-1]] <= array[i]:
            max_deque.pop()
        max_deque.append(i)

        while array[max_deque[0]] - array[min_deque[0]] > MAX_DIFF:
            start_index += 1
            if min_deque[0] < start_index:
                min_deque.popleft()
            if max_deque[0] < start_index:
                max_deque.popleft()

        max_length = max(max_length, i - start_index + 1)


                        
    return max_length
                
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().split()))
answer = solution(n, array)
print(answer)