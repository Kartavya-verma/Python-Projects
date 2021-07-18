n = int(input())
r = int(input())
t = [[0 for y in range(r + 1)] for x in range(n + 1)]
m = 1000000007
for i in range(n+1):
    for j in range(min(i,r)+1):
        if j == 0 or j == i:
            t[i][j] = 1
        else:
            t[i][j] = (t[i-1][j] + t[i-1][j-1])%m
print(t[n][r])