# baekjoon 10816 : 숫자 카드2
# solved by JY
# DATE : 2021.12.13
# Dictionary 사용

from collections import defaultdict
from sys import stdin
input = stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
dic = defaultdict(int)
for nnum in nlist:
    dic[nnum] += 1

for check in mlist:
    print(dic[check], end=' ')