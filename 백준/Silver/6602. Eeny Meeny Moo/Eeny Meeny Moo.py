import sys
from copy import deepcopy


def get_shutdown_order_array(length, m):
    answer = []
    already_shutdowned = set()
    array = list(range(1, length + 1))
    copied_array = deepcopy(array)

    index = 0
    while True:
        target = array[index]
        if target == 2 and len(copied_array) > 1:
            return False, []
        already_shutdowned.add(target)
        copied_array.remove(target)
        answer.append(target)
        if not copied_array:
            break
        index = (index + m)
        if index >= len(array):
            while index >= len(array):
                array.extend(copied_array)

    return True, answer


def solution(length):
    m = 1
    while True:
        success, ordered_array = get_shutdown_order_array(length, m)
        # print(success, ordered_array)
        if success and ordered_array[-1] == 2:
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