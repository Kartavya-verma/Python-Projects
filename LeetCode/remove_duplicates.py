# In place Array

nums = [0,0,1,1,1,2,2,3,3,4]
i = 0
for j in range(len(nums)):
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]
print(nums)
print(i+1)

