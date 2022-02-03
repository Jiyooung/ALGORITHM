# baekjoon 10845 : 큐
# solved by JY
# DATE : 2021.12.07
# 구현 - 큐 
# deque 사용 - queue는 동기화를 위해 만들어져서 deque에 비해 느림

from sys import stdin
input = stdin.readline
from collections import deque
que = deque()
for _ in range(int(input())):
    command = list(map(str, input().rstrip().split()))
    
    if command[0] == "push": que.append(command[1])
    elif command[0] == "pop": print(que.popleft() if que else -1)
    elif command[0] == "size": print(len(que))
    elif command[0] == "empty": print(0 if que else 1)
    elif command[0] == "front": print(que[0] if que else -1)
    else: print(que[-1] if que else -1)