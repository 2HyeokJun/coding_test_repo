import sys
from collections import deque

def get_element_to_save_or_pop(is_queue, existed_element, input_element):
    element_to_save = input_element if is_queue else existed_element
    element_to_pop = existed_element if is_queue else input_element
    return element_to_save, element_to_pop

def solution(length, questacktype_array, element_array, input_array_length, input_array):
    answer = []

    queuestack = deque()
    for i in range(0, length):
        questack_type = questacktype_array[i]
        existed_element = element_array[i]
        is_queue = questack_type == 0
        if is_queue:
            queuestack.append(existed_element)

    for i in range(0, input_array_length):
        element = input_array[i]
        queuestack.append(element)
        queuestack.rotate(-len(queuestack) + 1)
        popped = queuestack.pop()
        answer.append(str(popped))

    return " ".join(answer)

length = int(sys.stdin.readline())
questacktype_array = list(map(int, sys.stdin.readline().split()))
element_array = list(map(int, sys.stdin.readline().split()))
input_array_length = int(sys.stdin.readline())
input_array = list(map(int, sys.stdin.readline().split()))


answer = solution(
    length=length,
    questacktype_array=questacktype_array,
    element_array=element_array,
    input_array_length=input_array_length,
    input_array=input_array
)
print(answer)