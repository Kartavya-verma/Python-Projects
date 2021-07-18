# n = int(input())
# i = 1
# # num = 1
# y = 1
# while i <= n:
#     j = 1
#     while j <= n-i+1:
#        print("",end="")
#     print(j + 1, i)
#     # j=i
#     N=1
#     x=i
#     while(N<=i):
#         print("",end="")
#         x=x+1
#         N=N+1
#     p = 1
#     y=((2 * i)-1)
#     while(p<=i-1):
#         print(y,end="")
#         p=p+1
#         y=y+1
#     print()
#     i=i+1

n=int(input())
i=1
y=1
while(i<=n):
    j=1
    while(j<=n-1):
       print("",end="")
       j=j+1
    N=1
    x=i
    while(N<=i):
        print("",end="")
        x=x+1
        N=N+1
    p = 1
    y=((2 * i)-1)
    while(p<=i-1):
        print(y,end="")
        p=p+1
        y=y+1
    print()
    i=i+1