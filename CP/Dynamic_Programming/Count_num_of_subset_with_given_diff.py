def knapsack(wei,w,n):
    t = [[False for x in range(w + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if j == 0:
                t[i][j] = True
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wei[i-1] > j:
                t[i][j] = t[i-1][j]
            elif wei[i-1] <= j:
                t[i][j] = t[i-1][j-wei[i-1]] + t[i-1][j]
    # print(t)
    return t[n][w]


wei = [1,1,2,3]
diff = 1
w = (diff+sum(wei)) // 2
n = len(wei)
# t = [[False for x in range(w + 1)] for i in range(n + 1)]
# print(t)
ans = knapsack(wei,w,n)
print(ans)