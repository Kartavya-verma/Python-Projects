nums = [1, 1, 4, 2, 1, 3]
c= 0
for a, b in zip(nums, sorted(nums)):
    if a != b:
        c += 1
print(c)

# print(sum(a != b for a, b in zip(nums, sorted(nums))))