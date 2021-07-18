import sys
def knapsack(wei,w,n):
    t = [[0 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0:
                t[i][j] = sys.maxsize - 1
    for j in range(1,w+1):
        if j%wei[0] == 0:
            t[1][j] = j//wei[0]
        else:
            t[1][j] = sys.maxsize-1
    for i in range(2,n+1):
        for j in range(1,w+1):
            if wei[i-1] > j:
                t[i][j] = t[i-1][j]
            elif wei[i-1] <= j:
                t[i][j] = min(t[i][j-wei[i-1]] + 1,t[i-1][j])
    return t[n][w]


wei = [1,2,3]
w = 4
n = len(wei)
ans = knapsack(wei,w,n)
print(ans)