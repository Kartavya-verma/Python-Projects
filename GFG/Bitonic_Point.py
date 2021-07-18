def bitonic(li):
    l,r = 0, len(li)-1
    while l <= r:
        mid = l + (r-l)//2
        if mid == 0:
            return li[0] if li[mid] > li[mid+1] else li[1]
        if mid == len(li)-1:
            return li[len(li)-1] if li[mid] > li[mid - 1] else li[len(li)-2]
        if li[mid] > li[mid-1] and li[mid] > li[mid+1]:
            return li[mid]
        elif li[mid+1] > li[mid]:
            l = mid + 1
        elif li[mid-1] > li[mid]:
            r = mid - 1



li = [1,15,25,45,42,21,17,12,11]
print(bitonic(li))