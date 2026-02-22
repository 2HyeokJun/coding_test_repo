import sys


def solution(n, m, array):
    time = 0
    alcohol_sum = 0
    for i in range(n):
        alcohol = array[i]
        alcohol_sum += alcohol
        if (i+1) - m > 0:
            alcohol_sum -= array[i-m]
        if 129 <= alcohol_sum <= 138:
            time += 1

    return time
    
                
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
answer = solution(n, m, array)
print(answer)