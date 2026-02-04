import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())
outputs = []

for _ in range(T):
    N, index = map(int, input().split())

    arr = []
    while len(arr) < N:
        arr.extend(map(int, input().split()))
    arr = arr[:N]

    arr_deque = deque(arr)

    copied_arr = arr[:]
    copied_arr.sort(reverse=True)
    copied_arr_deque = deque(copied_arr)

    target_arr = [False] * len(arr)
    target_arr[index] = True
    target_arr_deque = deque(target_arr)

    count = 0
    while True:
        if arr_deque[0] == copied_arr_deque[0]:
            copied_arr_deque.popleft()
            arr_deque.popleft()
            count += 1
            if target_arr_deque[0]:
                break
            target_arr_deque.popleft()
        else:
            arr_deque.rotate(-1)
            target_arr_deque.rotate(-1)

    outputs.append(str(count))

print("\n".join(outputs))