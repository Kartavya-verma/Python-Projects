arr = [17,18,5,4,6,1]
for j in range(len(arr)-1):
    arr[j] = max(arr[j + 1:len(arr)])
arr[-1] = -1
print(arr)