nums = [1, 2, 3, 4]
mx = max(nums)
mx_ind = nums.index(mx)
for i in range(len(nums)):
    if i != mx_ind and nums[i] * 2 > mx:
        print(-1)
    print(mx_ind)