def searchRange(nums, target):
    if not nums:
        return [-1, -1]

    def bisect_left(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1

    def bisect_right(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        return l if nums[l] == target else -1

    return [bisect_left(nums, target), bisect_right(nums, target)]


l = [1,3,5,5,5,5,67,123,125]
x = 5
print(searchRange(l,x))