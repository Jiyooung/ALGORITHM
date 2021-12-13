# baekjoon 2562 : 최댓값
# solved by JY
# DATE : 2021.11.07
# Implementation

from sys import stdin
input = stdin.readline
num = [int(input()) for _ in range(9)]
MAX = max(num)
print(MAX)
print(num.index(MAX) + 1)