# baekjoon 1110 : 더하기 사이클
# solved by JY
# DATE : 2022.05.13
# Implementation

n = int(input())
num, ans = n, 1

while 1:
    num = (num%10)*10 + (num//10 + num%10)%10
    if num == n : break
    ans += 1

print(ans)