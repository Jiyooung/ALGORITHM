# baekjoon 3085 : 사탕 게임
# solved by JY
# DATE : 2021.04.08
# BruteForce 알고리즘
# swap 할때마다 모든 board 확인 > 시간 많이 걸림

import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(str, input().strip())) for _ in range(N)]

def allcheck(): # 모든 board 확인하는 함수
    cnt = 1
    for i in range(N):
        rtmp, ctmp = 1, 1
        for j in range(N-1):
            rtmp = rtmp + 1 if board[i][j] == board[i][j+1] else 1
            ctmp = ctmp + 1 if board[j][i] == board[j+1][i] else 1
            if cnt < rtmp: cnt = rtmp
            if cnt < ctmp: cnt = ctmp
    return cnt

def swap(r, c, nr, nc):
    tmp = board[r][c]
    board[r][c] = board[nr][nc]
    board[nr][nc] = tmp

ans = 1
for i in range(N):
    for j in range(N-1):
        if board[i][j] != board[i][j+1]:
            swap(i, j, i, j+1)  # 행
            ans = max(ans, allcheck())
            swap(i, j, i, j+1)
        if board[j][i] != board[j+1][i]:
            swap(j, i, j+1, i)  # 열
            ans = max(ans, allcheck())
            swap(j, i, j+1, i)
print(ans)
        