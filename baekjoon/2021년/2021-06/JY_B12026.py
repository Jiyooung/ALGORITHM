# baekjoon 12026 : BOJ 거리
# solved by JY
# DATE : 2021.06.15
# DP 알고리즘 사용
# dp[n] = n까지 가는데 드는 최소비용

from sys import stdin
input = stdin.readline
N = int(input())
board = list(map(str, input()))
dic = {'B':'J', 'O':'B', 'J':'O'}
dp = [1e9]*N
dp[0] = 0

for i in range(1, N):
    pre = dic[board[i]]
    for j in range(i):
        if board[j] == pre and dp[i] > dp[j] + (i - j)**2:
            dp[i] = dp[j] + (i - j)**2
    
print(-1) if dp[N-1] == 1e9 else print(dp[N-1])