# baekjoon 2621 : 카드게임
# solved by JY
# DATE : 2022.05.10
# Implementation
# Counter()와 most_common()

from sys import stdin
from collections import Counter
input = stdin.readline

colors, nums = [0]*5, [0]*5
for i in range(5): colors[i], nums[i] = input().rstrip().split(" ")
nums = list(map(int, nums))

sort_num = sorted(nums)
stair_flag = True
# 연속적인 숫자인지 확인 -> 연속이면 stair_flag = True
for i in range(1,5):
    if sort_num[i-1] + 1 != sort_num[i]:
        stair_flag = False
        break
cnt_col, cnt_num = Counter(colors), Counter(sort_num)

score = 0
# 두 가지 이상의 규칙을 적용할 수 있는 경우에는 가장 높은 점수가 카드 게임의 점수
# 1. 5장이 모두 같은 색이면서 숫자가 연속 -> 가장 높은 숫자 + 900
if len(cnt_col) == 1:
    if stair_flag : score = max(score, sort_num[-1] + 900)
    # 4. 5장의 카드 색깔이 모두 같을 때 -> 가장 높은 숫자 + 600
    else : score = max(score, sort_num[-1] + 600)

# 5. 5장의 숫자가 연속 -> 가장 높은 숫자 + 500
if stair_flag : score = max(score, sort_num[-1] + 500)

num_mc = cnt_num.most_common(2)

if len(cnt_num) == 2:
    # 2. 4장의 숫자가 같을 때 -> 같은 숫자 + 800
    if max(cnt_num.values()) == 4: score = max(score, num_mc[0][0] + 800)
    # 3. 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때 -> 3장 숫자 * 10 + 2장 숫자 + 700
    else: score = max(score, num_mc[0][0] * 10 + num_mc[1][0] + 700)
elif len(cnt_num) == 3:
    # 6. 3장의 숫자가 같을 때 -> 같은 숫자 + 400
    if max(cnt_num.values()) == 3: score = max(score, num_mc[0][0] + 400)
    # 7. 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 -> 같은 숫자 중 큰 숫자 * 10 + 작은 숫자 + 300
    else:
        a, b = num_mc[0][0], num_mc[1][0]
        if a > b: score = max(score, a * 10 + b + 300)
        else: score = max(score, b * 10 + a + 300)

# 8. 2장의 숫자가 같을 때 -> 같은 숫자 + 200
elif len(cnt_num) == 4: score = max(score, num_mc[0][0] + 200)

# 9. 위의 어떤 경우에도 해당하지 않을 때 -> 가장 높은 숫자 + 100
if score == 0: score = sort_num[-1] + 100

print(score)