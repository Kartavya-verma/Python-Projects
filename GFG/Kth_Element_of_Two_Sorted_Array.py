# def search(l1,l2,k):
#     l1.extend(l2)
#     l1.sort()
#     return l1[k-1]
#
#
def search(l1,l2,n,m,k):
    if n > m:
        return search(l2,l1,m,n,k)
    low = max(0,k-m)
    high = min(k,n)
    while low <= high:
        cut1 = (low + high) >> 1   # (low + high) // 2
        cut2 = k - cut1
        l1 = cut1 == 0 if float('-inf') else l1[cut1 - 1]
        l2 = cut2 == 0 if float('-inf') else l2[cut2 - 1]
        r1 = cut1 == n if float('inf') else l1[cut1]
        r2 = cut2 == m if float('inf') else l2[cut2]
        if l1 <= r2 and l2 <= r1:
            return max(l1,r2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return 1



l1 = [2,3,6,7,9]
l2 = [1,4,8,10]
k = 5
n = len(l1)
m = len(l2)
print(search(l1,l2,n,m,k))


