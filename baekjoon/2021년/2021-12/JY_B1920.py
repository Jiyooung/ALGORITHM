# baekjoon 1920 : 수 찾기
# solved by JY
# DATE : 2021.12.10
# BinarySearch

from sys import stdin
input = stdin.readline

n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))

def find(num):
    left, right = 0, len(array)
    while left < right:
        pos = (left + right) // 2

        if array[pos] == num:
            return 1
        elif array[pos] < num:
            left = pos + 1
        else:
            right = pos
    return 0

for num in check:
    print(find(num))
