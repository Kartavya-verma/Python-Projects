# def missing(a,b):
#     res = 0
#     for i in range(0, len(a)):
#         res = res ^ a[i]
#         print(res)
#     for i in range(0, len(b)):
#         res = res ^ b[i]
#         print(res)
#     # return res
#
# a = [1,2,3,4,5,10]
# b = [2,3,1,0,5]
# print(missing(a,b))




def findMissing(arr1, arr2, M, N):
    if (M != N - 1 and N != M - 1):
        print("Invalid Input")
        return

    res = 0
    for i in range(0, M):
        res = res ^ arr1[i];
    for i in range(0, N):
        res = res ^ arr2[i]

    print("Missing element is", res)


# Driver Code
arr1 = [4, 1, 5, 9, 7]
arr2 = [7, 5, 9, 4]
M = len(arr1)
N = len(arr2)
findMissing(arr1, arr2, M, N)

# This code is contributed
# by Smitha Dinesh Semwal
