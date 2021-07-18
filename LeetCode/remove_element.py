# Method - 1
# nums = [0,1,2,2,3,0,4,2]
# val = 2
#
# max_i = len(nums)-1
# # print(max_i)
# i = 0
# while i <= max_i:
#     # print(i,max_i)
#     if nums[i] == val:
#         nums.pop(i)
#         max_i -= 1
#     else:
#         i += 1
# print(nums)
# print(len(nums))


# METHOD - 2
nums = [0,1,2,2,3,0,4,2]
val = 2
while nums.count(val):
    nums.remove(val)
print(nums)
