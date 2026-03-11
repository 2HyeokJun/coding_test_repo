import sys



def solution(n, s, array):
    answer_set = set()
    small_index = 0
    big_index = n - 1
    for _ in range(n):
        small_element = array[small_index]
        big_element = array[big_index]

        sum = small_element + big_element
        if sum < s:
            small_index += 1
        elif sum == s and small_index != big_index:
            answer_set.add(small_element)
            answer_set.add(big_element)
            small_index += 1
            big_index -= 1
        else:
            big_index -= 1
        

    return len(answer_set) // 2 if len(answer_set) > 1 else len(answer_set)
    




    


n, s = map(int, sys.stdin.readline().split())
array = []
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

answer = solution(n, s, array)
print(answer)