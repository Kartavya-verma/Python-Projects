matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1
direction = 0

result = []
# direction = 0 ==> left to right
# direction = 1 ==> top to bottom
# direction = 2 ==> right to left
# direction = 3 ==> bottom to top

while top <= bottom and left <= right:
    if direction == 0:
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1
    elif direction == 1:
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1
    elif direction == 2:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1
    elif direction == 3:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1
    direction = (direction + 1) % 4
print(result)
