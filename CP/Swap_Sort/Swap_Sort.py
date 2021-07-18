# nums = [2, 3, 1, 8, 2, 3, 5, 1]
# x = 1
# for i in range(len(nums) - 1):
#     if nums[i] != nums[i + 1]:
#         nums[x] = nums[i + 1]
#         x += 1
# print(x)


l1 = [6,5,4,2,3,1]
i = 0
while i < len(l1):
    if l1[i] != l1[l1[i]-1]:
        temp = l1[l1[i]-1]
        l1[l1[i] - 1] = l1[i]
        l1[i] = temp
    else:
        i += 1
print(l1)