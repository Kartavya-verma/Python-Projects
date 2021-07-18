def knapsack(wei,w,n):
    t = [[0 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if j == 0:
                t[i][j] = 1
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wei[i-1] > j:
                t[i][j] = t[i-1][j]
            elif wei[i-1] <= j:
                t[i][j] = t[i][j-wei[i-1]] + t[i-1][j]
    return t[n][w]


wei = [1,2,3]
w = 4
n = len(wei)
ans = knapsack(wei,w,n)
print(ans)