nums = [1, 3, 4, 2, 2]
tortoise = hare = nums[0]
while True:
    tortoise = nums[tortoise]
    hare = nums[nums[hare]]
    if tortoise == hare:
        break

# Find the "entrance" to the cycle.
tortoise = nums[0]
while tortoise != hare:
    tortoise = nums[tortoise]
    hare = nums[hare]

print(hare)