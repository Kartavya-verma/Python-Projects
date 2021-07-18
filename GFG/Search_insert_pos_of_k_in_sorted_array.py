def search(l,k):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = low + (high-low)//2
        if l[mid] == k:
            return mid
        elif l[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return low

l = list(map(int,input().split()))
k = int(input())
print(search(l,k))