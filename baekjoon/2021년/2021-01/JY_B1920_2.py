# baekjoon 1920 : 수 찾기
# solved by JY
# DATE : 2021.01.27
# 이분탐색, python3으로 채점

def solution(num, l_idx, r_idx):
  flag = True
  while l_idx <= r_idx:
    mid_idx = int((l_idx + r_idx) / 2)
    if num == n_list[mid_idx]:
      print(1)
      flag = False
      break
    if num > n_list[mid_idx]:
      l_idx = mid_idx + 1
    else:
      r_idx = mid_idx - 1

  if flag:
    print(0)

# run test
N = int(input())
n_list = list(map(int, input().split(' ')))
M = int(input())
m_list = list(map(int, input().split(' ')))
n_list.sort()
for i in m_list:
  solution(i, 0, len(n_list) - 1)
