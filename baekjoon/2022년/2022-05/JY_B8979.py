# baekjoon 8979 : 올림픽
# solved by JY
# DATE : 2022.05.18
# Implementation

n, k = map(int, input().split(" "))
world = []
for i in range(n):
    num, g, s, b = map(int, input().split(" "))
    world.append([g, s, b, num])

world.sort(reverse=True)
answer, cnt = 0, 0
for i in range(n):
    if i != 0 and world[i-1][0:3] == world[i][0:3]:
        cnt += 1
    else:
        cnt = 0
    if world[i][3] == k:
        print(i - cnt + 1)
        break