# t=int(input())
# for i in range(t):
#     s=input()
#     if(len(s)%2==0):
#         mid=len(s)//2
#         l1=set([x for x in s[:mid]])
#         l2=set([x for x in s[mid:]])
#         if (l1 == l2):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         mid=len(s)//2
#         l1 = set([x for x in s[:mid]])
#         l2 = set([x for x in s[mid+1:]])
#         if(l1==l2):
#             print("YES")
#         else:
#             print("NO")
#

t=int(input())
for i in range(t):
    s=input()
    if(len(s)%2==0):
        mid=len(s)//2
        l1=[x for x in s[:mid]]
        l2=[x for x in s[mid:]]
        l1.sort()
        l2.sort()
        if(l1==l2):
            print("YES")
        else:
            print("NO")
    else:
        mid=len(s)//2
        l1 = [x for x in s[:mid]]
        l2 = [x for x in s[mid+1:]]
        l1.sort()
        l2.sort()
        if (l1 == l2):
            print("YES")
        else:
            print("NO")
