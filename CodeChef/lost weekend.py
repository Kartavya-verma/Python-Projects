t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    a=l.pop()
    l=[x*a for x in l]
    sum=0
    for i in l:
        sum+=i
    if (sum<=48):
        print("NO")
    elif(sum <=120):
        print("NO")
    else:
        print("YES")

# t=int(input())
# for i in range(t):
#     l=list(map(int,input().split()))
#     a=l.pop()
#     res=all(ele<=24 or ele<0 for ele in l)
#     if(res==True and (a<=24 or a>1)):
#         l=[x*a for x in l]
#         sum = 0
#         for i in l:
#             sum = sum + i
#         if (sum <=120):
#             print("NO")
#         else:
#             print("YES")

# l=[14,10,12,6,18,2]
# # l=[10,10,10,10,10,3]
# a=l.pop()
# l=[x*a for x in l]
# sum=0
# for i in l:
#     sum=sum+i
# # print(sum)
# # print(24*len(l))
# if(sum<=24*(len(l))):
#     print("NO")
# else:
#     print("YES")
