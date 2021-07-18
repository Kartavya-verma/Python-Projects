def subarray(l,n):
    s = 0
    hm = set()
    for i in range(n):
        s += l[i]
        if s == 0 or s in hm:
            print(True)
            exit()
        hm.add(s)
    print(False)


l = list(map(int,input().split()))
n = len(l)
print(subarray(l,n))