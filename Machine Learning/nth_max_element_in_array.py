def kthLargest(arr, n, k):
    arr.sort(reverse=True)
    print(arr)
    return arr[k - 1]


arr = list(map(int, input().split()))
n = len(arr)
k = int(input())
print("K'th Largest element is", kthLargest(arr, n, k))