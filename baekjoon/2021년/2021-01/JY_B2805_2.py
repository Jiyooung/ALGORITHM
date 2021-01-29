# baekjoon 2805 : 나무 자르기
# solved by JY
# DATE : 2021.01.28
# 이분탐색
import sys

def solution():
    answer, min_h, max_h = 0, 0, max(tree)
    while min_h <= max_h:
        mid_h = (min_h + max_h)//2 
        ret = sum(t-mid_h if t-mid_h > 0 else 0 for t in tree)

        if ret >= M:
            min_h, answer = mid_h + 1, mid_h
        else:
            max_h = mid_h - 1
            
    return answer

# run test
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
print(solution())
