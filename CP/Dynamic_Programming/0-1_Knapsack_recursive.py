def knapsack(val,wei,w,n):
    if n == 0 or w == 0:
        return 0
    elif wei[n-1] > w:
        return knapsack(val,wei,w,n-1)
    elif wei[n - 1] <= w:
        return max(val[n-1] + knapsack(val,wei,w-wei[n-1],n-1),knapsack(val,wei,w,n-1))


val = [60,100,120]
wei = [10,20,30]
w = 50
n = len(val)
ans = knapsack(val,wei,w,n)
print(ans)