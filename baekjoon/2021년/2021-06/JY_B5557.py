# baekjoon 5557 : 1학년
# solved by JY
# DATE : 2021.06.15
# DP 알고리즘 사용
# dp[i][j] = i번째에 j(0~20) 값이 나오는 경우의 수

from sys import stdin
input = stdin.readline
N = int(input())
num = list(map(int, input().split()))
dp = [[0]*21 for _ in range(N)]
dp[0][num[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j] != 0:
            if j + num[i] <= 20:
                dp[i][j + num[i]] += dp[i-1][j]
            if j - num[i] >= 0:
                dp[i][j - num[i]] += dp[i-1][j]

print(dp[N-2][num[-1]])
