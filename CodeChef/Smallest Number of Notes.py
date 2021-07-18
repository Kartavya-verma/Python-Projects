t=int(input())
rup=[100,50,10,5,2,1]
for i in range(t):
    temp = 0
    n=int(input())
    for j in rup:
        temp=temp+n//j
        n=n%j
    print(temp)
