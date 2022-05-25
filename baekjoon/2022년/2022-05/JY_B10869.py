# baekjoon 10869 : 사칙연산
# solved by JY
# DATE : 2022.05.25
# Implementation

a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, sep='\n')