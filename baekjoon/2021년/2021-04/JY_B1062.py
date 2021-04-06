# baekjoon 1062 : 가르침
# solved by JY
# DATE : 2021.04.01
# 조합 이용

import sys, itertools
input = sys.stdin.readline
N, K = map(int, input().split())
lang = [[] for _ in range(N)]
check, ans = set(), 0

if K >= 5:
    eng = set('antic')
    for idx in range(N):
        lang[idx] = set(input().strip()).difference(eng)
        check.update(lang[idx])

    if len(check) <= K - 5:
        ans = N
    else:
        for c in itertools.combinations(check, K - 5):
            c = set(c)
            cnt = 0
            for l in lang:
                if l.issubset(c):
                    cnt += 1
            
            ans = max(ans, cnt)

print(ans)