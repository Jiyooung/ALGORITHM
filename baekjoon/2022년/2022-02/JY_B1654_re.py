# baekjoon 1654 : 랜선 자르기
# solved by JY
# DATE : 2022.02.10
# BinarySearch
# 랜선의 길이를 추측하는 이분탐색 알고리즘

from sys import stdin
input = stdin.readline

k, n = list(map(int, input().split()))
line = sorted([int(input()) for _ in range(k)], reverse=True)

# check 함수 : 해당 mid값으로 N개의 랜선이 생성되는 지의 여부 확인
def check(num):
    cnt = 0
    for i in line:
        cnt += i // num
        if cnt >= n:
            return True
    return False

# 최대 랜선의 길이를 구하는 것 => 랜선의 길이 = mid
l, r = 0, line[0]
while l < r:
    mid = (l + r + 1) // 2
    if check(mid): l = mid
    else: r = mid - 1
print(l)