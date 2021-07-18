def max_abs(l):
    mn1 = float('inf')
    mn2 = float('inf')
    mx1 = float('-inf')
    mx2 = float('-inf')
    for i in range(len(l)):
        mx1 = max(mx1,l[i] + i)
        mn1 = min(mn1,l[i] + i)
        mx2 = max(mx2,l[i] - i)
        mn2 = min(mn2,l[i] - i)
    ans1 = mx1 - mn1
    ans2 = mx2 - mn2
    return max(ans1,ans2)


l = list(map(int,input().split()))
print(max_abs(l))