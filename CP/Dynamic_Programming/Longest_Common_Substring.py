def lcs(x, y, n, m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 0 or j == 0:
                t[i][j] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i - 1] == y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = 0
    mx = -1
    for i in range(n + 1):
        for j in range(m + 1):
            if t[i][j] > mx:
                mx = t[i][j]
    return mx


x = "abcdgh"
y = "abedfga"
n = len(x)
m = len(y)
t = [[0 for i in range(m+1)] for j in range(n+1)]
ans = lcs(x, y, n, m)
print(ans)