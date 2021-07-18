def wood(l,n,m):
    s = 0
    for i in range(n-1,-1,-1):
        if l[i] - m <= 0:
            break
        s += (l[i] - m)
    return s


def search(l,k):
    l.sort()
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = low + (high-low)//2
        res = wood(l,len(l),mid)
        if res == k:
            return mid
        elif res > k:
            low = mid + 1
        else:
            high = mid - 1
    return -1


l = list(map(int,input().split()))
k = int(input())
print(search(l,k))