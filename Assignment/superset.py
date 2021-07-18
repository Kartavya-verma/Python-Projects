n,m=map(int,input().split())
l1=map(int,input().split())
h=set(map(int,input().split()))
un=set(map(int,input().split()))
count=0
for i in l1:
    if(i in h):
        count+=1
    if(i in un):
        count-=1
print(count)