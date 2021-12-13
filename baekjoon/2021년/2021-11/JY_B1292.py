# baekjoon 1292 : 쉽게 푸는 문제
# solved by JY
# DATE : 2021.11.21
# Implementation

from sys import stdin
input = stdin.readline
start, end = map(int, input().split())
num = []
for i in range(46):
	num += [i] * i
print(sum(num[start-1:end]))