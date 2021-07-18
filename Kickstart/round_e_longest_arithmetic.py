# class Solution:
#     def Solve(self, A):
#         ans = 2
#         A = list(set(A))
#         n = len(A)
#         if n <= 2:
#             return n
#         llap = [2] * n
#         A.sort()
#
#         for j in range(n - 2, -1, -1):
#             i = j - 1
#             k = j + 1
#             while (i >= 0 and k < n):
#                 if A[i] + A[k] == 2 * A[j]:
#                     llap[j] = max(llap[k] + 1, llap[j])
#                     ans = max(ans, llap[j])
#                     i -= 1
#                     k += 1
#                 elif A[i] + A[k] < 2 * A[j]:
#                     k += 1
#                 else:
#                     i -= 1
#         return ans
#
#
# for i in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     obj = Solution()
#     res = obj.Solve(a)
#     print("Case #{}: {}".format(i+1, res))

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = a[0] - a[1]
    count = 0
    aa = []
    for j in range(len(a) + 1):
        if j < len(a) - 1:
            c = a[j] - a[j+1]
            if c == d:
                count += 1
                if j == len(a) - 2:
                    aa.append(count)
            else:
                d = c
                aa.append(count)
                count = 1
    print("Case "+ " " + "#" + str(i+1) + ":",max(aa)+1)