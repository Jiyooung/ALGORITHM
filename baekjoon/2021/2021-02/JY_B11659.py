# baekjoon 11659 : 구간 합 구하기 4
# solved by JY
# DATE : 2021.02.20
# DP 사용
# dp[i] = 1 ~ i번째까지의 합

# run test
import sys
input = sys.stdin.readline
N, M = map(int, input().split(" "))
num = list(map(int, input().split(" ")))
dp = []
for _ in range(M):
    s, e = map(int, input().split(" "))
    if len(dp) < e:
        for i in range(len(dp), e):
            dp.append(dp[-1] + num[i]) if len(dp) != 0 else dp.append(num[i])
    print(dp[e-1]) if s == 1 else print(dp[e-1]-dp[s-2])
