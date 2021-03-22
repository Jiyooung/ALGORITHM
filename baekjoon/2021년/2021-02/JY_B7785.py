# baekjoon 7785 : 회사에 있는 사람
# solved by JY
# DATE : 2021.02.23
# dictionary를 활용한 구현

# run test
import sys
input = sys.stdin.readline
n = int(input())
enter = {}
for i in range(n):
    name, inout = map(''.join, input().rstrip('\n').split(" "))
    if name not in enter:
        enter[name] = inout
    else:
        enter.pop(name)

enter = list(enter)
enter.sort(reverse=True)
for e in enter:
    print(e)
