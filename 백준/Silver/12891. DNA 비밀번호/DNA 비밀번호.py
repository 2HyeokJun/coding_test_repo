import sys

def is_possible_password(standard_dict, current_dict):
    return (
        standard_dict["A"] <= current_dict["A"] and
        standard_dict["C"] <= current_dict["C"] and
        standard_dict["G"] <= current_dict["G"] and
        standard_dict["T"] <= current_dict["T"]
    )


def solution(p, str, standard_dict):
    answer = 0
    curr_min_str_dict = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }
    start_str = str[:p]
    for char in start_str:
        curr_min_str_dict[char] += 1
    if is_possible_password(standard_dict, curr_min_str_dict):
        answer += 1

    for i, remain_char in enumerate(str[p:]):
        curr_min_str_dict[remain_char] += 1
        curr_min_str_dict[str[i]] -= 1
        if is_possible_password(standard_dict, curr_min_str_dict):
            answer += 1
    return answer

s, p = map(int, sys.stdin.readline().split())
str = sys.stdin.readline().rstrip()
min_a, min_c, min_g, min_t = map(int, sys.stdin.readline().split())
standard_dict = {
    "A": min_a,
    "C": min_c,
    "G": min_g,
    "T": min_t
}
answer = solution(p, str, standard_dict)
print(answer)
