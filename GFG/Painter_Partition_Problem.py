def numberOfPainters(arr, n, maxLen):
    total = 0
    numPainters = 1
    for i in arr:
        total += i
        if (total > maxLen):
            total = i
            numPainters += 1
    return numPainters

def partition(arr, n, k):
    lo = max(arr)
    hi = sum(arr)

    while lo < hi:
        mid = lo + (hi - lo) / 2
        requiredPainters = numberOfPainters(arr, n, mid)
        if (requiredPainters <= k):
            hi = mid
        else:
            lo = mid + 1
    return lo


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
k = 3
print(int(partition(arr, n, k)))
