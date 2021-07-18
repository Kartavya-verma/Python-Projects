m=set(map(int,input().split()))
n=int(input())
l=[]
for i in range(n):
    l.append(set(map(int,input().split())))
for i in l:
    if (i in m):
        print('True')
    else:
        print('False')