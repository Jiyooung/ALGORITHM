# baekjoon 1966 : 프린터 큐
# solved by JY
# DATE : 2022.01.17
# List, Counter

from sys import stdin
from collections import Counter
input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    count = Counter(seq)
    ans, flag, i = 0, 0, 0
    while seq:
        if i + ans == n: i = 0
        for j in range(9, seq[i], -1):
            if count[j] != 0:   # 중요도가 높은 문서가 있음 -> 다음 문서로 넘어감
                flag = 1
                break
        
        if flag: 
            i += 1
            flag = 0
            continue

        num = seq.pop(i)    # 문서 출력
        ans += 1            # 출력 문서 개수 + 1
        count[num] -= 1     # 중요도 갯수 처리
        if i < m: m -= 1    # 궁금한 문서 위치 조절
        elif i == m:
            print(ans)
            break