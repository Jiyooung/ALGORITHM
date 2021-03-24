# baekjoon 1541 : 잃어버린 괄호
# solved by JY
# DATE : 2021.03.24
# 정규표현식 사용

import sys, re
input = sys.stdin.readline
calc = list(map(str, input().rstrip('\n').split('-')))
calc = [re.sub('^0+','', cal) for cal in calc]        # 각 문자열 0으로 시작하는 부분 제거
calc = [re.sub('\+0+','+', cal) for cal in calc]      # +뒤에 나오는 0도 제거
calc = [re.sub('\++','+', cal) for cal in calc]       # 제거하면서 발생한 연산자의 만남 제거
calc = [re.sub('^[+]|[+]$','', cal) for cal in calc]  # 앞이나 뒤에 연산자가 존재 시 제거
calc = [eval(cal) for cal in calc]
print((calc[0]*2) - sum(calc))