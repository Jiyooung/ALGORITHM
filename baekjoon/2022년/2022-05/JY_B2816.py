# baekjoon 2816 : 디지털 티비
# solved by JY
# DATE : 2022.05.18
# Implementation

n = int(input())
chanel = list(input().rstrip() for i in range(n))
answer, flag = [], False
for i in range(n):
    if chanel[i] == 'KBS1':
        answer.extend([1]*i + [4]*i)
        break
    if chanel[i] == 'KBS2': flag = True

for i in range(n):
    if chanel[i] == 'KBS2':
        answer.extend([1]*(i + 1 if flag else i) + [4]*(i if flag else i-1))
        break

print(*answer, sep="")