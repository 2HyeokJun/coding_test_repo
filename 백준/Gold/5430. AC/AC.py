from collections import deque

class AC:
    def __init__(self, array):
        self.array = deque(array)
    def R(self):
        self.array.reverse()
    def D(self):
       if len(self.array) > 0:
           self.array.popleft()
       else:
           return "error"
    def print(self):
        return self.array
    

def solution(command, array):
    ac = AC(array)
    command = command.replace("RR", "")
    for c in command:
        if c == "R":
            ac.R()
        elif c == "D":
            if ac.D() == "error":
                return "error"
    return "[" + ",".join(map(str, ac.print())) + "]"

t = int(input())

out = []
for _ in range(t):
    command = input()
    n = int(input())
    s = input()

    if s == "[]":
        arr = []
    else:
        arr = list(map(int, s[1:-1].split(",")))

    out.append(solution(command, arr))

print("\n".join(out))