import sys


def solution(n, k, max_key, ice_dict):
    # k: 좌우 닿는 범위
    # max_key: 가장 멀리있는 양동이
    max_sum = 0
    for j in range(0, k):
        max_sum += ice_dict.get(j, 0)
    latest_sum = max_sum
    for i in range(0, max_key - k + 1):
        temp_sum = latest_sum + ice_dict.get(i+k, 0) - ice_dict.get(i-k-1, 0)
        max_sum = max(max_sum, temp_sum)
        latest_sum = temp_sum
    

    return max_sum

n, k = map(int, sys.stdin.readline().split())
ice_dict = {}
max_key = 0
for _ in range(0, n):
    # key: 좌표, value: 얼음양
    value, key = map(int, sys.stdin.readline().split())
    ice_dict[key] = value
    max_key = max(max_key, key)
answer = solution(n, k, max_key, ice_dict)
print(answer)