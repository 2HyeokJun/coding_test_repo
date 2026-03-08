import sys
from collections import Counter

def _mathematics_average(list, length):
    return round(sum(list)/length)

def _median(sorted_list, length):
    return sorted_list[length // 2]

def _mode(list):
    counter = Counter(list).most_common()
    most_common_array = []
    max_count = counter[0][1]
    for c in counter:
        if c[1] == max_count:
            most_common_array.append(c[0])
        else:
            break

    most_common_array.sort()
    return most_common_array[1] if len(most_common_array) > 1 else most_common_array[0]

def _range(sorted_list):
    return sorted_list[-1] - sorted_list[0]



def solution(n, array, sorted_array):
    mathematics_average = _mathematics_average(array, n)
    median = _median(sorted_array, n)
    mode = _mode(array)
    range = _range(sorted_array)

    return mathematics_average, median, mode, range


n = int(sys.stdin.readline().rstrip())
array = []
sorted_array = []
for i in range(n):
    element = int(sys.stdin.readline().rstrip())
    array.append(element)
    sorted_array.append(element)

sorted_array.sort()

answer = solution(n, array, sorted_array)
print(answer[0])
print(answer[1])
print(answer[2])
print(answer[3])