def knapsack(val,wei,w,n):
    t = [[0 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wei[i-1] > j:
                t[i][j] = t[i-1][j]
            elif wei[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i][j-wei[i-1]],t[i-1][j])
    return t[n][w]


val = [1,6,18,22,28]
wei = [1,2,5,6,7]
w = 11
n = len(val)
ans = knapsack(val,wei,w,n)
print(ans)