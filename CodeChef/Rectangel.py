# t=int(input())
# for i in range(t):
#     l=list(map(int,input().split()))
#     for j in l:
#         temp=j
#         if(temp in l):
#

# def findPairs(lst, k):
#     return [(e1, e2) for e1 in lst for e2 in lst if (e1 - e2 == k)]
#
#
# # Driver code
# lst = [1,1,2,2]
# k = 0
# print(findPairs(lst, k))

# t=int(input())
# for i in range(t):
#     l=list(map(int,input().split()))
#     if(len(set(l))==2):
#         li=[]
#         for i in l:
#             li.append(l.count(i))
#         if(2 in set(li) and len(set(li))==1):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")

t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    l.sort()
    if(l[0]==l[1] and l[2]==l[3]):
        print("YES")
    else:
        print("NO")