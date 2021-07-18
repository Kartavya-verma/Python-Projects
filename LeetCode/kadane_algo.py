arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = arr[0]
current_sum = max_sum
for i in range(1, len(arr)):
    current_sum = max(arr[i] + current_sum, arr[i])
    max_sum = max(current_sum, max_sum)
print(max_sum)