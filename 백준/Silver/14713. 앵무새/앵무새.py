import sys

input = sys.stdin.readline

N = int(input().strip())

S = []
for _ in range(N):
    # 각 앵무새 문장: 단어 리스트로 저장
    S.append(input().strip().split())

# 받아 적은 문장 L
L = input().strip().split()

for l in L:
    popped = False
    for s in S:
        if len(s) and s[0] == l:
            s.pop(0)
            popped = True
            break
    if not popped:
        print("Impossible")
        break

if popped:
    is_all_empty = True
    for s in S:
        if s:
            is_all_empty = False
            print("Impossible")
            break
    if is_all_empty and popped:
        print("Possible")