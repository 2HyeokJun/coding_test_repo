from collections import deque
import sys

student_deque = deque()
length = int(sys.stdin.readline())

for i in range(0, length):
    student_name, student_id = sys.stdin.readline().split()
    student_id = int(student_id)
    student_deque.append((student_name, student_id))


def solution(student_deque):
    while len(student_deque) > 1:
        standard = student_deque.popleft()
        student_id = standard[1]
        pass_count = (student_id -1) * (-1)
        student_deque.rotate(pass_count)
        student_deque.popleft()
    return student_deque[0][0]

answer = solution(student_deque)
print(answer)