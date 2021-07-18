while True:
    n=int(input())
    if n!=0:
        li=list(map(int,input().split()))
        li1=[0]*len(li)
        for i in range(len(li)):
            li1[li[i]-1]=i+1
        if(li1==li):
            print("ambiguous")
        else:
                print("not ambiguous")
    else:
        break

# print(li)
# print(li1)

# li=list(map(int,input().split()))
# l1=[]*len(li)
# for i in range(len(li)):
#     l1.insert(li[i],i)
# print(l1)


# 1.
# l=list(map(int,input().split()))
# a=[0]*len(l)
# for i in range(len(l)):
#     a[l[i]-1]=i+1
#     if a==l:
#         print("ambiguous")
#     else:
#         print("not ambiguous")


# 2.
# while int(input()) != 0:
#     arr = list(map(int, input().split()))
#     for i in range(len(arr)):
#         x = arr[i]
#         if arr[x-1] != i+1:
#             print ("not ambiguous")
#             break
#     else:
#         print ('ambiguous')