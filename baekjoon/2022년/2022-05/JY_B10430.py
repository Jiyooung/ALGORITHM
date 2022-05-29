# baekjoon 10430 : 나머지
# solved by JY
# DATE : 2022.05.29
# Implementation

A, B, C = map(int, input().split())
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
