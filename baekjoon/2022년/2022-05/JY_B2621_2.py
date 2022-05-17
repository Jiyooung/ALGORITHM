# baekjoon 2621 : 카드게임
# solved by JY
# DATE : 2022.05.12
# Implementation
# Best Answer 참고

from sys import stdin
input = stdin.readline

colors, nums = [], []

for i in range(5):
    a, b = input().rstrip().split(" ")
    colors.append(a)
    nums.append(int(b))

colors.sort()
nums.sort()
ans = []

# 두 가지 이상의 규칙을 적용할 수 있는 경우에는 가장 높은 점수가 카드 게임의 점수
# 1. 5장이 모두 같은 색이면서 숫자가 연속 -> 가장 높은 숫자 + 900
if colors[0] == colors[-1] and nums[-1] - nums[0] == 4: ans.append(nums[-1] + 900)
# 2. 4장의 숫자가 같을 때 -> 같은 숫자 + 800
if nums[0] == nums[3] or nums[1] == nums[-1]: ans.append(nums[1] + 800)
# 3. 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때 -> 3장 숫자 * 10 + 2장 숫자 + 700
if nums[0] == nums[2] and nums[3] == nums[4]: ans.append(nums[2] * 10 + nums[-1] + 700)
if nums[0] == nums[1] and nums[2] == nums[4]: ans.append(nums[2] * 10 + nums[0] + 700 )
# 4. 5장의 카드 색깔이 모두 같을 때 -> 가장 높은 숫자 + 600
if colors[0] == colors[-1]: ans.append(nums[-1] + 600)
# 5. 5장의 숫자가 연속 -> 가장 높은 숫자 + 500
if nums[0] + 4 == nums[1] + 3 == nums[2] + 2 == nums[3] + 1 == nums[4]: ans.append(nums[-1] + 500)
# 6. 3장의 숫자가 같을 때 -> 같은 숫자 + 400
if nums[0] == nums[2] or nums[1] == nums[3] or nums[2] == nums[4]: ans.append(nums[2] + 400)
# 7. 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 -> 같은 숫자 중 큰 숫자 * 10 + 작은 숫자 + 300
if (nums[0] == nums[1] and (nums[2] == nums[3] or nums[3] == nums[4])) or (nums[1] == nums[2] and nums[3] == nums[4]):
    ans.append(nums[3] * 10 + nums[1] + 300)
# 8. 2장의 숫자가 같을 때 -> 같은 숫자 + 200
if nums[0] == nums[1]: ans.append(nums[0] + 200)
if nums[1] == nums[2]: ans.append(nums[1] + 200)
if nums[2] == nums[3]: ans.append(nums[2] + 200)
if nums[3] == nums[4]: ans.append(nums[3] + 200)
# 9. 위의 어떤 경우에도 해당하지 않을 때 -> 가장 높은 숫자 + 100
ans.append(nums[-1] + 100)

print(sorted(ans)[-1])