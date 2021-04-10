# baekjoon 17070 : 파이프 옮기기 1
# solved by JY + best
# DATE : 2021.04.10
# DP 알고리즘 사용
# cnt[i][j][0,1,2] = (i,j)에 해당 방향(0,1,2)으로 들어올 수 있는 경우의 수

from sys import stdin
input = stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
cnt = [[[0,0,0] for _ in range(N)] for _ in range(N)]
cnt[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if board[i][j] == 0: 
            cnt[i][j][0] = cnt[i][j-1][0] + cnt[i][j-1][2]

            if i > 0:
                cnt[i][j][1] = cnt[i-1][j][1] + cnt[i-1][j][2]

                if board[i-1][j] == 0 and board[i][j-1] == 0:
                    cnt[i][j][2] = cnt[i-1][j-1][0] + cnt[i-1][j-1][1] + cnt[i-1][j-1][2]

print(sum(cnt[N-1][N-1]))

