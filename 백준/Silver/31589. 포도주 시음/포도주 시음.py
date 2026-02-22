import sys
from collections import deque


def solution(n, k, array):
    array.sort()
    deq = deque(array)

    answer = 0
    start = 0
    last_wine = 0
    while start < k:
        wine = deq.pop() if start % 2 == 0 else deq.popleft()   # 홀수번째는 최대 와인을, 짝수번째에는 최소 와인을 꺼낸다.
        answer += (wine - last_wine) if wine >= last_wine else 0
        last_wine = wine
        start += 1
            
    return answer
                
n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
answer = solution(n, k, array)
print(answer)