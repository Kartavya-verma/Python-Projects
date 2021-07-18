t=int(input())
for i in range(t):
    n=int(input())
    n1=map(int,input().split())
    n1=set(n1)
    m=int(input())
    m1=map(int,input().split())
    m1=set(m1)
    if(n1.issubset(m1)):
        print('True')
    else:
        print('False')
