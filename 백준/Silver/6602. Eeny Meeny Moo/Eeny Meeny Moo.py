import sys
from copy import deepcopy


def get_shutdown_order_array(length, m):
    answer = []
    already_shutdowned = set()
    array = list(range(1, length + 1))
    copied_array = deepcopy(array)

    index = 0
    while True:
        already_shutdowned.add(array[index])
        copied_array.remove(array[index])
        answer.append(array[index])
        if not copied_array:
            break
        index = (index + m)
        if index >= len(array):
            while index >= len(array):
                array.extend(copied_array)

    return answer


def solution(length):
    m = 1
    while True:
        ordered_array = get_shutdown_order_array(length, m)
        if ordered_array[-1] == 2:
            break
        m += 1
    return m



answer_array = []
while True:
    length = int(sys.stdin.readline())
    if length == 0:
        break
    answer = solution(length)
    answer_array.append(str(answer))
print('\n'.join(answer_array))