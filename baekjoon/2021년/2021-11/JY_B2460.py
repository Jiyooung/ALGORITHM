# baekjoon 2460 : 지능형 기차 2
# solved by JY
# DATE : 2021.11.21
# Implementation

from sys import stdin
input = stdin.readline
answer, now = 0, 0

for _ in range(10):
	off, on = map(int, input().split())
	now += -off + on
	answer = max(answer, now)

print(answer)