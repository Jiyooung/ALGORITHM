# baekjoon 11724 : 연결 요소의 개수
# solved by JY
# DATE : 2022.05.18
# Implementation

from collections import defaultdict
from sys import stdin
input = stdin.readline

n, m = map(int, input().split(" "))

num = [0]*(n+1)
group = defaultdict(list)
cnt_group, cnt_empty, cnt_dot = 0, 0, n

for _ in range(m):
    u, v = map(int, input().split(" "))
    if num[u] + num[v] == 0:
        cnt_group += 1
        num[u] = cnt_group
        num[v] = cnt_group
        group[cnt_group].extend([u, v])
        cnt_dot -= 2
    elif num[u] == num[v]:
        continue
    elif num[u] == 0 or num[v] == 0:
        if num[u] == 0: 
            f, to = u, v
        else: 
            f, to = v, u
        num[f] = num[to]
        group[num[to]].append(f)
        cnt_dot -= 1
    else:
        if len(group[num[u]]) < len(group[num[v]]): 
            f, to = u, v
        else: 
            f, to = v, u
        
        del_group = num[f]
        for idx in group[del_group]:
            num[idx] = num[to]

        group[num[to]].extend(group[del_group])
        group[del_group] = []
        cnt_empty += 1

print(cnt_group - cnt_empty + cnt_dot)