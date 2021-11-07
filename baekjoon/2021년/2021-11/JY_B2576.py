# baekjoon 2576 : 홀수
# solved by JY
# DATE : 2021.11.07
# 구현

from sys import stdin
input = stdin.readline
num = [int(input()) for _ in range(7)]
odd = [n for n in num if n%2 == 1]
if len(odd) == 0: print(-1)
else: print(sum(odd), min(odd), sep="\n")
