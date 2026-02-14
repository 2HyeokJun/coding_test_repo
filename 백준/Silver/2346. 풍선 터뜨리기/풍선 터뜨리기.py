import sys
from collections import deque



def solution(paper_dict, deq):
    popped_array = []
    index = 1
    popped_array.append(deq[0])
    deq[0] = None

    start_count = 0
    while len(popped_array) < length:
        next_index = paper_dict[index]
        direction = -1 if next_index > 0 else 1
        count = next_index * direction * (-1)
        while start_count < count:
            deq.rotate(direction)
            if deq[0] != None:
                start_count += 1
        popped_array.append(deq[0])
        index = deq[0]
        deq[0] = None
        start_count = 0

    return popped_array

length = int(sys.stdin.readline())
paper_array = list(map(int, sys.stdin.readline().split()))
paper_dict = {}
deq = deque()
for i in range(1, length + 1):
    paper_dict[i] = paper_array[i - 1]
    deq.append(i)

answer = solution(paper_dict, deq)
print(*answer)