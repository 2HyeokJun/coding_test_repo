import sys

from collections import deque

def solution(fork, knife, customer_list, deque_length):
    fork_deque = deque([None] * deque_length)
    knife_deque = deque([None] * deque_length)

    i = 1
    while customer_list:
        # print("fork:", fork_deque, fork)
        # print("knife:", knife_deque, knife)
        popped = fork_deque.popleft()
        if popped is not None:
            count = popped[1]
            fork += count
        popped = knife_deque.popleft()
        if popped is not None:
            count = popped[1]
            knife += count

        if customer_list[0][0] == i:
            customer = customer_list.pop(0)
            stay_time = customer[1]
            order = customer[2]
            is_need_knife = order == 1
            if fork == 0 or (is_need_knife and knife == 0):
                print("No")
                i += 1
                continue
            fork -= 1
            if is_need_knife:
                knife -= 1

            if fork_deque[stay_time - 1] is not None:
                count = fork_deque[stay_time - 1][1]
                fork_deque[stay_time - 1] = ("fork", count + 1)
            else:
                fork_deque[stay_time - 1] = ("fork", 1)
            if is_need_knife:
                if knife_deque[stay_time - 1] is not None:
                    count = knife_deque[stay_time - 1][1]
                    knife_deque[stay_time - 1] = ("knife", count + 1)
                else:
                    knife_deque[stay_time - 1] = ("knife", 1)
            print("Yes")
        i = i + 1


fork, knife, customer_count = map(int, sys.stdin.readline().split())
customer_list = []
max_a = 0
max_b = 0
for i in range(0, customer_count):
    (a, b, c) = map(int, sys.stdin.readline().split())
    customer_list.append((a, b, c))
    max_a = max(max_a, a)
    max_b = max(max_b, b)

deque_length = max_a + max_b
answer = solution(fork, knife, customer_list, deque_length)
