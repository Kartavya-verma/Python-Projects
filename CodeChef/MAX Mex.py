for j in range(int(input())):
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    n=len(li)
    for i in range(n):
        if (li[i] <= 0 or li[i] > n):
            continue
        val = li[i]
        while (li[val - 1] != val):
            nextval = li[val - 1]
            li[val - 1] = val
            val = nextval
            if (val <= 0 or val > n):
                break
    for i in range(n):
        if (li[i] != i + 1):
            mex= i + 1
    mex= n + 1

    if(mex==m):
        print(mex)
    else:
        print("-1")