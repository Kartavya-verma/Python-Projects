# for i in range(int(input())):
# #     n=int(input())
# #     l=list(map(int,input().split()))
# #     c=0
# #     temp=0
# #     for j in range(len(l)-1):
# #         while ((j - 1) != -1):
# #             if(l[j]>l[j+1] and l[j]>l[j-1]):
# #                     temp=temp+1
# #             j=j-1
# #         if(temp>0):
# #             c=c+1
# #     print(c)

t = int(input())
p = t + 1
while t != 0:
    n = int(input())
    a = list(map(int, input().split()))
    maxi = max(a)
    pos = a.index(maxi)
    r = 0
    for j in range(pos + 1):
        if len(set(a))==1:
             r = 0
        elif maxi == a[-1] or maxi == a[0]:
            r = 1
        elif a[j] > a[j + 1]:
            r += 1
    print("Case #{}: {}".format(p-t,r))
    t -= 1