def maximize(l,k):
    s,max_one,zero = 0,0,0
    for e in range(len(l)):
        if l[e] == 0:
            zero += 1
        while zero > k:
            if l[s] == 0:
                zero -= 1
            s += 1
        max_one = max(max_one,e-s+1)
    return max_one


l = list(map(int,input().split()))
k = int(input())
print(maximize(l,k))