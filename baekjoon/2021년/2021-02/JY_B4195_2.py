# baekjoon 4195 : 친구 네트워크
# solved by JY
# DATE : 2021.02.24
# Union-Find 사용
# parent : { name : [부모, 친구 수] }

def find(p):
    if p == parent[p][0]:
        return p
    parent[p][0] = find(parent[p][0])
    return parent[p][0]

def union(a, b):
    a_p, b_p = find(a), find(b)
    if a_p != b_p:  # 다른 그룹일 때 합치기
        parent[b_p][0] = a_p
        parent[a_p][1] += parent[b_p][1]

# run test
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    F = int(input())
    parent = {}

    for _ in range(F):
        f1, f2 = input().split()

        if f1 not in parent:
            parent[f1] = [f1, 1]
        if f2 not in parent:
            parent[f2] = [f2, 1]
        
        union(f1, f2)
        print(parent[parent[f1][0]][1])
        