import sys
from collections import deque
from copy import deepcopy



def get_count_and_popped_deque(deq: deque, target: int):
    count = 0
    if deq[0] == target:
        deq.popleft()
        return count, deq

    left_deque = deepcopy(deq)
    right_deque = deepcopy(deq)

    while True:
        left_deque.rotate(-1)
        count += 1
        right_deque.rotate(1)
        if left_deque[0] == target:
            left_deque.popleft()
            return count, left_deque
        if right_deque[0] == target:
            right_deque.popleft()
            return count, right_deque
        
def solution(length, target_array):
    answer  = 0
    init_deq = deque(list(range(1, length + 1)))
    for target in target_array:
        count, deq = get_count_and_popped_deque(init_deq, target)
        answer += count
        init_deq = deq
    return answer


deque_length, target_array_length = map(int, sys.stdin.readline().split())
target_array = list(map(int, sys.stdin.readline().split()))

answer = solution(deque_length, target_array)
print(answer)