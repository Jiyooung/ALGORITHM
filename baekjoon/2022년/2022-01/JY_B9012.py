# baekjoon 9012 : 괄호
# solved by JY
# DATE : 2022.01.18
# Stack

from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    ps = str(input().rstrip())
    stack = []
    for p in ps:
        if p == "(":
            stack.append(p)
        else:
            if stack and stack[-1] == "(":
                stack.pop(-1)
            else:
                stack.append(-1)
                break
    
    if stack: print("NO")
    else: print("YES")
