import sys


def _dict_to_str(dict):
    string = ""
    for key, value in dict.items():
        string += f"{key}{str(value)}"
    return string


def _counter(current_counter, plus_char, minus_char):
    current_counter[plus_char] += 1
    if minus_char is not None:
        current_counter[minus_char]-= 1

    counter_str = _dict_to_str(current_counter)

    return current_counter, counter_str







def solution(k, w):
    answer = 1
    answer_dict = {}
    counter_dict = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }
    for i in range(k):
        counter_dict[w[i]] += 1
    default_str = _dict_to_str(counter_dict)
    answer_dict[default_str] = 1
    
    for i in range(k, len(w)):
        plus_char = w[i]
        minus_char = w[i - k]
        counter_dict, string = _counter(counter_dict, plus_char, minus_char)
        count = answer_dict.get(string, 0) + 1
        answer_dict[string] = count
        answer = max(count, answer)
        
    
    return answer

t = int(sys.stdin.readline().rstrip())
answer_array = []
for i in range(t):
    k, w = map(str, sys.stdin.readline().split())
    answer = solution(int(k), w)
    answer_array.append(answer)


for answer in answer_array:
    print(answer)