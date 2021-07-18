def lcs(x, y, n, m):
    if n == 0 or m == 0:
        return 0
    elif t[n][m] != -1:
        return t[n][m]

    elif x[n - 1] == y[m - 1]:
        t[n][m] = 1 + lcs(x, y, n - 1, m - 1)
        return t[n][m]
    else:
        t[n][m] = max(lcs(x, y, n - 1, m), lcs(x, y, n, m - 1))
        return t[n][m]


x = "abcdgh"
y = "abedfga"
n = len(x)
m = len(y)
t = [[-1 for i in range(m+1)] for j in range(n+1)]
ans = lcs(x, y, n, m)
print(ans)