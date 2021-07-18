def knapsack(val,wei,w,n):
    if n == 0 or w == 0:
        return 0
    if t[n][w] != -1:
        return t[n][w]
    elif wei[n-1] > w:
        t[n][w] = knapsack(val,wei,w,n-1)
        return t[n][w]
    elif wei[n-1] <= w:
        t[n][w] = max(val[n-1] + knapsack(val,wei,w-wei[n-1],n-1),knapsack(val,wei,w,n-1))
        return t[n][w]


val = [60,100,120]
wei = [10,20,30]
w = 50
n = len(val)
# t = [[0]*(w+1)]*(n+1)
t = [[-1 for i in range(w+1)] for j in range(n+1)]
# print(t)
ans = knapsack(val,wei,w,n)
print(ans)