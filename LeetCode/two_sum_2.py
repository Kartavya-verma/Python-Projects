numbers = [2, 7, 11, 15]
target = 9
left = 0
right = len(numbers) - 1
res = []
while left < right:
    if numbers[left] + numbers[right] == target:
        res.append(left + 1)
        res.append(right + 1)
        break
    elif numbers[left] + numbers[right] < target:
        left += 1
    else:
        right -= 1
print(res)