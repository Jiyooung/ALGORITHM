# baekjoon 1946 : 신입 사원
# solved by JY
# DATE : 2021.03.24
# Greedy
# 나보다 서류 순위가 높은 모든 사람들보다 나의 면접 순위가 높아야한다.

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    scores = [[0, 0] for _ in range(N)]
    for idx in range(N):
        scores[idx] = list(map(int, input().split()))

    scores = sorted(scores)
    mini, cnt = scores[0][1], 1
    for score in scores[1:]:
        if score[1] < mini:
            mini = score[1]
            cnt += 1
        if mini == 1:
            break
    print(cnt)
