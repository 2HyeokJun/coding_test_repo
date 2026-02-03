import sys

class Queue:
    def __init__(self):
        self.queue = []
    def push(self, x):
        self.queue.append(x)
    def pop(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[0])
            self.queue.pop(0)
    def size(self):
        print(len(self.queue))
    def empty(self):
        print(1) if len(self.queue) == 0 else print(0)
    def front(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[0])
    def back(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[-1])

queue = Queue()
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        queue.push(int(cmd[1]))
    elif cmd[0] == "pop":
        queue.pop()
    elif cmd[0] == "size":
        queue.size()
    elif cmd[0] == "empty":
        queue.empty()
    elif cmd[0] == "front":
        queue.front()
    elif cmd[0] == "back":
        queue.back()