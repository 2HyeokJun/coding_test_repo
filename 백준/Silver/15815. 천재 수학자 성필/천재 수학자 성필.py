import sys


str = sys.stdin.readline().rstrip()

def is_operator(char):
    return char == "+" or char == "-" or char == "*" or char == "/"        

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num2 - num1
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return int(num2/num1)
    
def solution(str):
    int_array = []
    for char in str:
        if not is_operator(char):
            int_array.append(int(char))
        else:
            num1 = int_array.pop()
            num2 = int_array.pop()
            calculate_result = calculate(num1, num2, char)
            int_array.append(calculate_result)
    return int_array[0]


result = solution(str)
print(result)