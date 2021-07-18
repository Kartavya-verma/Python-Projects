'''for i in range(0,5,1):
    for j in range(0,5,1):
        if j<=i:
            print("*",end="")
    print()'''

'''for i in range(6):
    for j in range(6-i):
            print("*",end="")
    print()'''

q=int(input("Enter a num: "))
for i in range(2,q):
        if q%i==0:
            print("Not a prime num")
            break
else:
    print("Prime num")