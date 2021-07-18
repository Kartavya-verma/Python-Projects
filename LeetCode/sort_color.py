nums = [2, 0, 2, 1, 1, 0]
z = nums.count(0)
o = nums.count(1)
t = nums.count(2)
nums.clear()
for i in range(z):
    nums.append(0)
for i in range(o):
    nums.append(1)
for i in range(t):
    nums.append(2)
print(nums)