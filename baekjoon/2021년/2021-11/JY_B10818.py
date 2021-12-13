# baekjoon 10818 : 최소, 최대
# solved by JY
# DATE : 2021.11.18
# Implementation

from sys import stdin
input = stdin.readline
n = int(input())
num = list(map(int, input().split(' ')))
print(min(num), max(num))