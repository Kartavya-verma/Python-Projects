
from math import gcd
from functools import reduce

t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    l=l[1:]
    x=reduce(gcd,l)
    # print(x)
    if x==1:
        for i in l:
            print(i,end=" ")
        print()
    else:
        l1=[y//x for y in l]
        for i in l1:
            print(i,end=" ")
        print()
















