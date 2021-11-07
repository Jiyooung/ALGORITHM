# baekjoon 1546 : 평균
# solved by JY
# DATE : 2021.11.07
# 구현

from sys import stdin
input = stdin.readline
N = int(input())
score = list(map(int, input().split()))
MAX = max(score)
print(sum([s/MAX*100 for s in score])/N)