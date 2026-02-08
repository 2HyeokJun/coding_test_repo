from collections import deque
import copy
import sys

def solution(str):
    answer = ""
    temp_deque = deque()
    
    is_tag_opened = False
    for char in str:
        if char == "<":
            is_tag_opened = True
            for temp_char in copy.deepcopy(temp_deque):
                popped = temp_deque.popleft()
                answer += popped
        if is_tag_opened:
            answer += char
        elif char != " ":
            temp_deque.appendleft(char)
        if char == ">":
            is_tag_opened = False
        if not is_tag_opened and char == " ":
            for temp_char in copy.deepcopy(temp_deque):
                popped = temp_deque.popleft()
                answer += popped
            answer += " "

    for temp_char in copy.deepcopy(temp_deque):
        popped = temp_deque.popleft()
        answer += popped
    return answer
        
str = sys.stdin.readline().rstrip()
answer = solution(str)
print(answer)