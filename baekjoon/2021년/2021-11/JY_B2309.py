# baekjoon 2309 : 일곱 난쟁이
# solved by JY
# DATE : 2021.11.21
# BruteForce
# 9개합 - 100 = 거짓난쟁이 둘의 합

from sys import stdin
input = stdin.readline
num = sorted([int(input()) for _ in range(9)])

def solution(mysum):
	for i in range(8):
		for j in range(i + 1, 9):
			if num[i] + num[j] == mysum:
				a, b = num[i], num[j]
				num.remove(a)
				num.remove(b)
				return num

# run test
num = solution(sum(num)-100)
for n in num:
	print(n)