# baekjoon 11724 : 연결 요소의 개수
# solved by JY
# DATE : 2022.05.18
# Union-Find

from sys import stdin
input = stdin.readline

n, m = map(int, input().split(" "))
p = [0]*(n+1)
for i in range(n+1): p[i] = i

def find(v):
    if p[v] == v: return v
    
    p[v] = find(p[v])
    return p[v]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa != pb: p[pb] = pa

for i in range(m):
    u, v = map(int, input().split(" "))
    union(u, v)

answer = set()
for i in range(1, n+1):
    answer.add(find(i))

print(len(answer))