nums = [4,3,2,7,8,2,3,1]
# li = [x for x in range(nums[0], nums[-1]+1) if x not in nums]
# print(li)
# li = []
# for i in range(1, len(nums) + 1):
#     if i not in nums:
#         li.append(i)
# print(li)

for i in range(len(nums)):
    j = abs(nums[i]) - 1
    nums[j] = abs(nums[j]) * -1
res = []
for i in range(len(nums)):
    if nums[i] > 0:
        res.append(i+1)
print(res)
