# baekjoon 2751 : 수 정렬하기 2
# solved by JY
# DATE : 2022.05.20
# Implementation
# pypy3으로 채점!

from sys import stdin
input = stdin.readline

n = int(input())
print(*sorted([int(input()) for _ in range(n)]), sep='\n')