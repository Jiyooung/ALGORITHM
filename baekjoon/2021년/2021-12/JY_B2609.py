# baekjoon 2609 : 최대공약수와 최소공배수
# solved by JY
# DATE : 2021.12.09
# 수학
# 유클리드호제법(Euclidean) - 최대공약수
# 나누는 수와 나머지로 나누는 과정을 되풀이하여 나머지가 0이 될 때, 최대공약수를 알 수 있다.
# 최소공배수 = 두 수의 곱 / 최대공약수

from sys import stdin
input = stdin.readline
a, b = map(int, input().split())


# a, b중 크기 상관없음 -> b가 더 커도 gcd(b, a) 호출
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

gcd_ans = gcd(a, b)
print(gcd_ans, int(a*b/gcd_ans), sep='\n')