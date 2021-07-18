# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     h = list(map(int, input().split()))
#     h.sort(reverse=True)
#     r = []
#     flag = 0
#     print(h)
#     # h = [20, 19, 10, 8, 8, 7, 7, 7] 1st test case
#     # h = [10, 9, 4, 2] 2nd test case
#     s = h[0]
#     c = 0
#     for i in h:
#         if h:
#             if s < k and c < k:
#                 c += i
#                 r.append(i)
#                 # h.remove(i)
#             elif s > k:
#                 r.append(h[0])
#             else:
#                 s = 0
#     # print(s)
#     print(len(r))


# cook your dish here
# for _ in range(int(input())):
#     n,k = map(int,input().split())
#     h = list(map(int,input().split()))
#     h.sort()
#     if len(h) < 2:
#         print(-1)
#     else:
#         mick = []
#         tracy = []
#         mick.append(h[len(h)-1])
#         tracy.append(h[len(h)-2])
#         count = 2
#         print(mick)
#         print(tracy)
#         # h = [20, 19, 10, 8, 8, 7, 7, 7] 1st test case
#         #  h = [10, 9, 4, 2] 2nd test case
#         for i in range(len(h)-3,-1,-2):
#             if sum(mick) < k:
#                 mick.append(h[i])
#                 count += 1
#                 print("mick",mick)
#             if i-1>=0 and sum(tracy)<k:
#                 tracy.append(h[i-1])
#                 count+=1
#                 print("tracy", tracy)
#             print(i,sum(tracy),sum(mick))
#             i-=1
#             print(i)
#         # #print(mick)
#         # #print(tracy)
#         # if sum(mick)>=k and sum(tracy)>k:
#         #     print(count)
#         # else:
#         #     print(-1)

# for _ in range(int(input())):
#     n,k = map(int,input().split())
#     h = list(map(int,input().split()))
#     h.sort(reverse=True)
#     if len(h) < 2:
#         print(-1)
#     else:
#         mick = []
#         tracy = []
#         mick.append(h[0])
#         tracy.append(h[1])
#         count = 2
#         # print(mick)
#         # print(tracy)
#         # h = [20, 19, 10, 8, 8, 7, 7, 7] 1st test case
#         #  h = [10, 9, 4, 2] 2nd test case
#         for i in range(2, len(h) + 1, 2):
#             if sum(mick) < k:
#                 mick.append(h[i])
#                 count += 1
#                 print("mick",mick)
#             if i+1 < len(h) and sum(tracy) < k:
#                 tracy.append(h[i+1])
#                 count += 1
#                 print("tracy", tracy)
#             print(i, sum(tracy), sum(mick))
#             i += 1
#             print(i)
#         print(mick)
#         print(tracy)
#         if sum(mick) >= k and sum(tracy) > k:
#             print(count)
#         else:
#             print(-1)


# for _ in range(int(input())):
#     n,k = map(int,input().split())
#     h = list(map(int,input().split()))
#     h.sort(reverse=True)
#     s = 0
#     r = []
#     total =
#     if s < 2 * k:
#         for i in h:
#             s += i
#             r.append(i)
#     print(len(r))





# Latest
# cook your dish here
for _ in range(int(input())):
    n, k = map(int,input().split())
    h = list(map(int,input().split()))
    h.sort()
    if sum(h) < (2 * k) or len(h) < 2:
        print(-1)
    elif sum(h) == (2 * k):

        print(len(h))
    elif sum(h) > (2 * k):
        count, sum1 = 2, h[len(h)-1] + h[len(h)-2]
        for i in range(len(h)-3, -1, -1):
            #print(sum_,count)
            if (sum1 // 2) >= k:
                break
            sum1 += h[i]
            count += 1
        if (sum1 // 2) >= k:
            print(count)
        else:
            print(-1)
