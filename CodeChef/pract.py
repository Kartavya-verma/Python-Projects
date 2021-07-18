for i in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    r=0
    li1=[]
    if(max(li)==li[-1]):
        r=r+1
        print(r)
    # for j in range(li.index(max(li))):
    li1.append(li[li.index(max(li)):-1:-1])
    print(li1)



















# li=list(map(int,input().split()))
# for i in range(len(li)-1):
#     c=0
#     if(li[i]>li[i+1]):
#         # print(li[i],li[i+1])
#         if(i!=0):
#             for j in range(i,0,-1):
#                 if(li[i]>li[j]):
#                     c=c+1
#                     print("c=",c,li[i],li[j])
#     if(c==i):
#         print("final",li[i])