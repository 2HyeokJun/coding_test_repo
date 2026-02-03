n, k = map(int, input().split())
array = list(range(1, n + 1))

index = 0
target = k - 1
length = len(array)
answer = []
while length > 0:
    if index >= length + 1:
        index = length % index
    pop_target = (index + target) % length
    answer.append(str(array[pop_target]))
    array.pop(pop_target)
    index = pop_target
    length = len(array)
print(f"<{", ".join(answer)}>")