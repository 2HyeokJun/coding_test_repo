import sys


def solution(list):
    round = 1
    index = 1
    
    start_index = 0
    while len(list) > 1:
        have_to_turn = round ** 3
        
        target_index = (have_to_turn % len(list) - 1) - ((len(list) - start_index) % len(list))
        if target_index < 0:
            target_index += len(list)
        list.pop(target_index)
        round += 1
        start_index = target_index

        
    return list[0]

input = int(sys.stdin.readline())
array = list(range(1, input + 1))

answer = solution(array)
print(answer)