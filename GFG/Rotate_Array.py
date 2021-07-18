def reverse(l,s,e):
    while s <= e:
        l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1
    return l

def rotate(l,n,d):
    reverse(l,0,n-1)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    return l


# n = int(input())
# d = int(input())
# l = list(map(int,input().split()))
n = 7
d = 3
l =[1,2,3,4,5,6,7]
print(rotate(l,n,d))
