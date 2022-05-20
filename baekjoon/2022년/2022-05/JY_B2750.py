# baekjoon 2750 : 수 정렬하기
# solved by JY
# DATE : 2022.05.20
# Implementation

n = int(input())
print(*sorted([int(input()) for _ in range(n)]), sep='\n')