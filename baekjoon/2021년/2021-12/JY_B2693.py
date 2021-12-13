# baekjoon 2693 : N번째 큰 수
# solved by JY
# DATE : 2021.12.10
# Implementation

from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    print(sorted(list(map(int, input().split())))[-3])