# baekjoon 15486 : 퇴사 2
# solved by JY
# DATE : 2021.04.29
# DP 알고리즘 사용
# DP[i] = i + 1 일부터 시작했을 때에 얻을 수 있는 최대 수익
# 두 번의 for문으로 시간 소요 높음

from sys import stdin
input = stdin.readline
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)

if schedule[N-1][0] == 1:
    dp[N-1] = schedule[N-1][1]

for i in range(N-2, -1, -1):
    if i + schedule[i][0] > N:
        dp[i] = dp[i+1]
        continue
    dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i + 1])

print(dp[0])