# baekjoon 2609 : 최대공약수와 최소공배수
# solved by JY
# DATE : 2022.02.09
# 수학

from sys import stdin
input = stdin.readline

n1, n2 = map(int, input().split())

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

ret = gcd(n1, n2)
print(ret, (n1*n2)//ret, sep="\n")
