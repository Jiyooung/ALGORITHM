# baekjoon 15486 : 퇴사 2
# solved by JY + best
# DATE : 2021.04.29
# DP 알고리즘 사용
# DP[i] = i + 1 일까지 일했을 때에 얻을 수 있는 최대 수익

from sys import stdin
input = stdin.readline
N = int(input())
dp = [0]*(N+1)
MAX = 0
for i in range(N):
    t, p = map(int, input().split())
    MAX = max(MAX, dp[i])
    if i + t <= N and dp[i + t] < p + MAX:
        dp[i + t] = p + MAX

print(max(dp))