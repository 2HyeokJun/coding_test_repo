import sys

def solution(a, b, a_arr, b_arr):
    a_arr.sort()
    b_arr.sort()

    answer = 0
    a_index = 0
    b_index = 0
    while a_index <= a - 1:
        while b_index <= b - 1 and a_arr[a_index] > b_arr[b_index]:
            b_index += 1
        if b_index > 0:
            answer += b_index
        a_index += 1
    return answer

total_answer = []
question_length = int(sys.stdin.readline())
for _ in range(question_length):
    a, b = map(int, sys.stdin.readline().split())
    a_arr = list(map(int, sys.stdin.readline().split()))
    b_arr = list(map(int, sys.stdin.readline().split()))
    answer = solution(a, b, a_arr, b_arr)
    total_answer.append(answer)

for answer in total_answer:
    print(answer)