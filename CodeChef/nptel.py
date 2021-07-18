# n, m = map(int,input().split())
# l = list()
# for i in range(n):
#     l.append(input())
# print(l)
# l = list(zip(*l))
# s = ''
# print(l)
# for i in l:
#     s = s+''.join(i)
#     print(s)
# s = s.replace(" ", "")
# print(s)
# ans = ""
# for i in s:
#     if i.isalnum():
#        ans += i
# print(ans)


# vocab = {}
# li = input().split()
# for i in li:
#     if not vocab.get(i, None):
#         vocab[i] = 1
#     else:
#         vocab[i] += 1
#
# print(len(vocab), end=" ")
# for i in vocab.values():
#     print(i, end="")

# d = {}
# li = input().split()
# for i in li:
#     if not d.get(i, None):
#         d[i] = 1
#     else:
#         d[i] += 1
# print(len(d), end=" ")
# for i in d.values():
#     print(i, end="")

# nums = [2,0,2,1,1,0]
# l = 0
# r = len(nums) - 1
# i = 0
# while i <= r and l < r:
#     if nums[i] == 0:
#         nums[i] = nums[l]
#         nums[l] = 0
#         i += 1
#         l += 1
#     elif nums[i] == 2:
#         nums[i] = nums[r]
#         nums[r] = 2
#         r -= 1
#     else:
#         i += 1

# nums = [2,0,2,1,1,0]
# l = 0
# r = len(nums) - 1
# i = 0
# # while i <= r :
# if nums[i] == 0:
#     nums[i] = nums[l]
#     nums[l] = nums[i]
#     i += 1
#     l += 1
# print(nums[i], nums[l])
# # elif nums[i] == 2:
# #     nums[i] = nums[r]
# #     nums[r] = 2
# #     r -= 1
# # else:
# #     i += 1
# print(nums[i], nums[l])

nums = [2,5,3,6,8,9]
nums[1],nums[2] = nums[2],nums[1]
print(nums[1],nums[2])
