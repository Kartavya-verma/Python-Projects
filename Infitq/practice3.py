n = int(input())
mat = []
for i in range(n):
  li = list(map(int, input().split()))
  mat.append(li)

r = n
c = len(li)

res = []

for i in range(r):
  for j in range(c-3):
    if(mat[i][j]==mat[i][j+1]==mat[i][j+2]==mat[i][j+3]):
      res.append(mat[i][j])

for j in range(c):
  for i in range(r-3):
    if(mat[i][j]==mat[i+1][j]==mat[i+2][j]==mat[i+3][j]):
      res.append(mat[i][j])

for i in range(r-3):
  for j in range(c-3):
    if(mat[i][j]==mat[i+1][j+1]==mat[i+2][j+2]==mat[i+3][j+3]):
      res.append(mat[i][j])

for i in range(r-3):
  for j in range(c-3,c):
    if(mat[i][j]==mat[i-1][j-1]==mat[i-2][j-2]==mat[i-3][j-3]):
      res.append(mat[i][j])

if(len(res)==0):
  print("-1")
else:
  res.sort()
  print(res[0])