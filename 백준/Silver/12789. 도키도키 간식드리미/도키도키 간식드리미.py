from collections import deque
import copy
import sys

N = int(sys.stdin.readline().rstrip())
num_deque = deque(map(int, input().split()))



def solution(N, num_deque):
    start = 1
    space_list = []
    while start < N:
        # space_list의 마지막 인원이거나 num_deque의 첫번째 인원이거나
        if (num_deque and num_deque[0] == start) or (space_list and space_list[-1] == start):
            # num_deque이면: 앞에서 빼고
            if num_deque and num_deque[0] == start:
                num_deque.popleft()
            # space_list면: 뒤에서 뺀다
            else:
                space_list.pop()
            start += 1
        # 실패시: num_deque의 앞에서 빼서 space_list의 뒤에 넣고 재시도한다
        else:
            if len(num_deque) == 0:
                return "Sad"
            space_list.append(num_deque.popleft())
    return "Nice"
        
answer = solution(N, num_deque)
"""
5
5 4 1 3 2
"""
print(answer)