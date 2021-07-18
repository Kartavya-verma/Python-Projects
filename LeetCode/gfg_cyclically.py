n = 5
arr = [1, 2, 3, 4, 5]
temp = arr[n-1]
for i in range(n-1, -1, -1):
    arr[i] = arr[i-1]
arr[0] = temp
print(arr)