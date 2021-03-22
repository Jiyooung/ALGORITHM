# baekjoon 1920 : 수 찾기
# solved by JY
# DATE : 2021.01.27
# 완전탐색, pypy3으로 채점

def solution():    
    for i in m_list:
      if i in n_list:
        print(1)
      else:
        print(0)

# run test
N = int(input())
n_list = list(map(int, input().split(' ')))
M = int(input())
m_list = list(map(int, input().split(' ')))
solution()