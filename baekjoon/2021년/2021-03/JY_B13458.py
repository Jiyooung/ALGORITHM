# baekjoon 13458 : 시험 감독
# solved twice by JY
# DATE : 2021.03.26
# Greedy 알고리즘, dictionary 사용

import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans, dic = 0, {}
for a in A:
    if a in dic:
        ans += dic[a]
    elif a > B:
        dic[a] = (a - B)//C + 1 if (a - B)%C > 0 else (a - B)//C
        ans += dic[a]
print(ans + N)
