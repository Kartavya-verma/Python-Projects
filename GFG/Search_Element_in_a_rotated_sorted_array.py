def bitonic(li,k):
    l,r = 0, len(li)-1
    while l <= r:
        mid = l + (r-l)//2
        if li[mid] == k:
            return mid
        if li[l] <= li[mid]:
            if li[l] <= k <= li[mid]:
               r = mid - 1
            else:
                l = mid + 1
        else:
            if li[mid] <= k <= li[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

li = [3,1,2]
k = 1
print(bitonic(li,k))