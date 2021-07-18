n=int(input())

matrix = [list(map(int,input().split())) for i in range(n)]

if not len(matrix):
    pass
top = 0
bottom = len(matrix)-1
left = 0
right = len(matrix[0])-1
while(left < right and top < bottom):
    prev = matrix[top+1][left]
    for i in range(left, right+1):
        curr = matrix[top][i]
        matrix[top][i] = prev
        prev = curr
    top += 1
    for i in range(top, bottom+1):
        curr = matrix[i][right]
        matrix[i][right] = prev
        prev = curr
    right -= 1
    for i in range(right, left-1, -1):
        curr = matrix[bottom][i]
        matrix[bottom][i] = prev
        prev = curr
    bottom -= 1
    for i in range(bottom, top-1, -1):
        curr = matrix[i][left]
        matrix[i][left] = prev
        prev = curr
    left += 1
matrix=matrix
for i in range(n):
    for j in range(n-1):
        print(matrix[i][j],end=" ")
    if(i==n-1 and j+1==n-1):
        print(matrix[i][j+1],end="")
    else:
        print(matrix[i][j+1])