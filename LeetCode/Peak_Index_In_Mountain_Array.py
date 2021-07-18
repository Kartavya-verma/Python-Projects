def bitonic(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return left


li = [1,15,25,45,42,21,17,12,11]
print(bitonic(li))