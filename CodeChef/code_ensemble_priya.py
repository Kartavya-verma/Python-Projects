# for _ in range(int(input())):
#     n = int(input())
#     li = list(map(int, input().split()))
#     res = []
#     for i in range(len(li)-1):
#         for j in range(len(li)):
#
#             res.append(i,j)
#             # res.append(li[i] & li[i+1])
#     print(res)

# def countPairs(a, n):
#     count = 0
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if (a[i] & a[j]) == a[i]:
#                 count += 1
#     return count


for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if (li[i] & li[j]) == li[i]:
                count += 1
    print(count)
    # print(countPairs(li, len(li)))