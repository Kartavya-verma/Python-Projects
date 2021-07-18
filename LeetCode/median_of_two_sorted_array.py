nums1 = [1, 2]
nums2 = [3, 4]
nums1.extend(nums2)
nums1.sort()
if len(nums1) % 2 != 0:
    print(nums1[len(nums1)//2])
else:
    n = len(nums1) // 2
    avg = (nums1[n-1] + nums1[n]) / 2
    print(avg)