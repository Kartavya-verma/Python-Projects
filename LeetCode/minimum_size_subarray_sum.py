from sys import maxsize

nums = [2,3,1,2,4,3]
s = 7

res = maxsize

left = 0
val = 0

for i in range(len(nums)):
    val += nums[i]

    while val >= s:
        res = min(res, i+1-left)
        val -= nums[left]
        left += 1

# if res != maxsize:
#     print(res)
# else:
#     print(0)

print(res if res != maxsize else 0)