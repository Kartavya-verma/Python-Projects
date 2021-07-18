# arr = [2, 2, 3, 1]
# arr = list(set(arr))
# arr.sort(reverse=True)
# print(arr)
# if len(arr) < 3:
#     print(max(arr))
# else:
#     print(arr[2])

arr = [2, 2, 3, 1]
arr = list(set(arr))
arr.sort()
print(arr)
if len(arr) < 3:
    print(max(arr))
else:
    print(arr[-3])
