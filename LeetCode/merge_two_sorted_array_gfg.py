# def merge(one, two, one_size, two_size):
#     i = one_size - 1
#     j = 0
#     while i >= 0 and j < two_size:
#         if one[i] > two[j]:
#             temp = one[i]
#             one[i] = two[j]
#             two[j] = temp
#         i -= 1
#         j += 1
#     return sorted(one), sorted(two)
#
#
# l1 = [1, 3, 5, 7]
# l2 = [0, 2, 6, 8, 9]
# l3, l4 = merge(l1, l2, len(l1), len(l2))
# print(l3, l4)


def nextGap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)  #ceil value => ceil(gap/2)


def merge(arr1, arr2, n, m):
    gap = n + m
    gap = nextGap(gap)
    while gap > 0:
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1
        gap = nextGap(gap)


a1 = [10, 27, 38, 43, 82]
a2 = [3, 9]
n = len(a1)
m = len(a2)
merge(a1, a2, n, m)
print("First Array: ", end="")
for i in range(n):
    print(a1[i], end=" ")
print()
print("Second Array: ", end="")
for i in range(m):
    print(a2[i], end=" ")
print()