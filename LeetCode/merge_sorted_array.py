nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
if n == 0:
    pass
nums1[-n:] = nums2
nums1.sort()

print(nums1)