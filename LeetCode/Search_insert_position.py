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

l = [-12,-11,-3,5,6,15,16,18]
k = 19
print(search(l,k))