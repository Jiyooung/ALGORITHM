# baekjoon 12845 : 모두의 마블
# solved twice by JY
# DATE : 2021.03.26
# Greedy 알고리즘

import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
maxidx = card.index(max(card))
ans = 0
for idx in range(0, maxidx):
    ans += card[idx] + card[maxidx]
for idx in range(maxidx+1, n):
    ans += card[idx] + card[maxidx]
print(ans)
