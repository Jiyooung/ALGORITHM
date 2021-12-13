# baekjoon 2805 : 나무 자르기
# solved by JY
# DATE : 2021.12.13
# BinarySearch

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
tree = sorted(list(map(int, input().split())))

def check(mid):  # mid로 잘랐을 경우 m 이상의 나무를 얻을 수 있다면 True 리턴
    ans = 0
    for i in range(n-1, -1, -1):
        if tree[i] - mid > 0:
            ans += tree[i] - mid
        if ans >= m:
            return True
    return False

def find():
    answer = 0
    left, right = 0, max(tree)

    while left <= right:
        mid = (left + right) // 2
        if check(mid):  # mid로 조건 만족
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    return answer

print(find())