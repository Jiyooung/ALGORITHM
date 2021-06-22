# baekjoon 11058 : 크리보드
# solved by JY
# DATE : 2021.06.15
# DP 알고리즘 사용
# dp[n] = n번 눌렀을 때 최대 A개수
# dp[j]를 Ctrl-V 한 횟수 = (i - j - 2)
# dp[j] + dp[j] * (i - j - 2) = dp[j] * (i - j - 2 + 1) = dp[j] * (i - j - 1)

from sys import stdin
input = stdin.readline
N = int(input())
dp = [i+1 for i in range(N)]

for i in range(3, N):
    for j in range(i - 3, -1, -1):
        dp[i] = max(dp[i], dp[j] * (i - j - 1))

print(dp[N-1])