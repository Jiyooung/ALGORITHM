# baekjoon 1652 : 누울 자리를 찾아라
# solved by JY
# DATE : 2022.05.04
# Implementation

from sys import stdin
input = stdin.readline

n = int(input())
room = [str(input().rstrip()) for _ in range(n)]
r_ans, c_ans = [0]*n, [0]*n

for row in range(n):
    for col in range(n):
        if room[row][col] == "X": continue
        if row < n - 1 and room[row+1][col] == ".":
            if row == 0 or room[row-1][col] == "X":
                c_ans[col] += 1
        if col < n - 1 and room[row][col+1] == ".":
            if col ==0 or room[row][col-1] == "X":
                r_ans[row] += 1

print(sum(r_ans), sum(c_ans))
