nums = [1, 4, 3, 2]
nums.sort()
s = 0
for i in range(len(nums)):
    if i % 2 == 0:
        s += nums[i]
print(s)