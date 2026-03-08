import sys


def _vowel(char):
    return char in ["a", "e", "i", "o", "u", "y"]

def solution(k, sentence):
    continuous_vowel_array = []
    vowel = 0
    for char in sentence:
        if _vowel(char):
            vowel+= 1
        elif vowel != 0:
            continuous_vowel_array.append(vowel)
            vowel = 0
            
    if vowel != 0:
        continuous_vowel_array.append(vowel)

    answer = 0
    for vowel_count in continuous_vowel_array:
        answer += max((vowel_count - k + 1), 0)

    return answer


z = int(sys.stdin.readline().rstrip())
for i in range(z):
    k, sentence = sys.stdin.readline().split()
    answer = solution(int(k), sentence)
    print(answer)