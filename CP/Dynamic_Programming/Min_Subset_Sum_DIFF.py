import sys
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
                t[i][j] = t[i-1][j-wei[i-1]] or t[i-1][j]
    # print(t)
    return t[n]


wei = [1,6,11,5]
w = sum(wei)
n = len(wei)
# t = [[False for x in range(w + 1)] for i in range(n + 1)]
# print(t)
ans = knapsack(wei,w,n)
print(ans)

sub1=[]
for i in range((w//2)+1):
    if ans[i]==True:
        sub1.append(i)
print(sub1)

mn=sys.maxsize
for i in range(len(sub1)):
    mn=min(mn,w-2*sub1[i])
print(mn)