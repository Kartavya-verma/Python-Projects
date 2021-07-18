# N = 4
#
# def transpose(A, B):
#     for i in range(N):
#         for j in range(N):
#             B[i][j] = A[j][i]
#
#         # driver code
#
#
# A = [[1, 2, 9, 13],
#      [5, 6, 10, 14],
#      [3, 7, 11, 15],
#      [4, 8, 12, 16]]
#
# B = A[:][:]
#
# transpose(A, B)
#
# print("Result matrix is")
# for i in range(N):
#     for j in range(N):
#         print(B[i][j], " ", end='')
#     print()

for _ in range(int(input())):
    n = int(input())
    two_d = []
    for _ in range(n):
        li = list(map(int, input().split()))
        two_d.append(li)
    for i in range(n-1, 0, -1):
        if two_d
    print(two_d)