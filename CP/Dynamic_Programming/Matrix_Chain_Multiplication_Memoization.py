import sys


def solve(arr,i,j):
    if i >= j:
        return 0
    if t[i][j] != -1:
        return t[i][j]
    mn = sys.maxsize
    for k in range(i,j):
        temp = solve(arr,i,k)+solve(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        if temp < mn:
            mn = temp
    t[i][j] = mn
    return t[i][j]


arr = [40,20,30,10,30]
i = 1
j = len(arr)-1
t = [[-1 for x in range(1001)]for y in range(1001)]
print(solve(arr,i,j))