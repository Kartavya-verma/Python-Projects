import sys


def solve(arr,i,j):
    if i >= j:
        return 0
    mn = sys.maxsize
    for k in range(i,j):
        temp = solve(arr,i,k)+solve(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        if temp < mn:
            mn = temp
    return mn


arr = [40,20,30,10,30]
i = 1
j = len(arr)-1
print(solve(arr,i,j))