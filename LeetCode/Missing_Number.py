nums = [0]
n = [0]*10
for i in range(len(nums)):
    n[nums[i]] += 1
for i in range(len(nums)):
    if n[i] == 0:
        print(i)
print(len(nums))