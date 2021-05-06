# baekjoon 15989 : 1,2,3 더하기 4
# solved by JY + hint
# DATE : 2021.05.06
# DP 알고리즘 사용
# dp[n][0] = 오름차순으로 n 표현 시 1로 끝나는 경우의 수 = dp[n-1][0]
# dp[n][1] = 오름차순으로 n 표현 시 2로 끝나는 경우의 수 = dp[n-2][0] + dp[n-2][1]
# dp[n][2] = 오름차순으로 n 표현 시 3로 끝나는 경우의 수 = dp[n-3][0] + dp[n-3][1] + dp[n-3][2]

from sys import stdin
input = stdin.readline
T = int(input())
dp = [[0]*3 for _ in range(10001)]
dp[1][0] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 1
dp[3][1] = 1
dp[3][2] = 1
cnt = 4

for i in range(T):
    n = int(input())
    
    if n >= cnt:
        for idx in range(cnt, n+1):
            dp[idx][0] = dp[idx-1][0]
            dp[idx][1] = dp[idx-2][0] + dp[idx-2][1]
            dp[idx][2] = dp[idx-3][0] + dp[idx-3][1] + dp[idx-3][2]
        cnt = n

    print(dp[n][0] + dp[n][1] + dp[n][2])
