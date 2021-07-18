# Method - 1  Self
a = [4, 3, 2, 7, 8, 2, 3, 1]
a.sort()
li = []
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        li.append(a[i+1])
print(li)

# Method - 2 Youtube
# a = [4, 3, 2, 7, 8, 2, 3, 1]
# res = []
# for n in a:
#     n = abs(n)
#     if a[n-1] > 0:
#         a[n-1] *= -1
#     else:
#         res.append(n)


# Method - 3 Sets
# nums = [4,3,2,7,8,2,3,1]
# s = set()
# l = []
# for i in nums:
#     if i not in s:
#         s.add(i)
#     else:
#         l.append(i)
# print(l)

# Wrong Method of Sets TLE Storage Problem

# nums = [4,3,2,7,8,2,3,1]
# s = set(nums)
# l = []
# for i in s:
#     if nums.count(i) == 2:
#         l.append(i)
# print(l)

# Method - 4 Same as Method 3 Trying

# nums = [4,3,2,7,8,2,3,1]
# l = []
# l1 = []
# for i in nums:
#     if i not in l1:
#         l1.append(i)
#     else:
#         l.append(i)
# print(l)