nums = [1, 7, 3, 6, 5, 6]
total = 0
for i in nums:
    total += i

left = 0
for i in range(len(nums)):
    if i != 0:
        left += nums[i - 1]
    # print(left , total - left - nums[i], nums[i])
    if total - left - nums[i] == left:
        print(i)
print(-1)