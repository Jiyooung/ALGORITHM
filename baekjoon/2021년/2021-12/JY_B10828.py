# baekjoon 10828 : 스택
# solved by JY
# DATE : 2021.12.16
# 구현 - 스택

from sys import stdin
input = stdin.readline
stack = []
for _ in range(int(input())):
    command = list(map(str, input().rstrip().split()))
    
    if command[0] == "push": stack.append(command[1])
    elif command[0] == "pop": print(stack.pop() if stack else -1)
    elif command[0] == "size": print(len(stack))
    elif command[0] == "empty": print(0 if stack else 1)
    else: print(stack[-1] if stack else -1)