# baekjoon 10866 : 덱
# solved by JY
# DATE : 2021.12.07
# 구현 - 덱
# deque 사용 - queue는 동기화를 위해 만들어져서 deque에 비해 느림

from collections import deque
from sys import stdin
input = stdin.readline
dque = deque()
for _ in range(int(input())):
    command = list(map(str, input().rstrip().split()))

    if command[0] == "push_front": dque.appendleft(command[1])
    elif command[0] == "push_back": dque.append(command[1])
    elif command[0] == "pop_front": print(dque.popleft() if dque else -1)
    elif command[0] == "pop_back": print(dque.pop() if dque else -1)
    elif command[0] == "size": print(len(dque))
    elif command[0] == "empty": print(0 if dque else 1)
    elif command[0] == "front": print(dque[0] if dque else -1)
    else: print(dque[-1] if dque else -1)
