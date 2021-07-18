def isPrime(s):
    if s==2:
      return True
    for i in range(2,s):
        if(s%i==0):
            return False
            break
    return True

# t=int(input())
# if(isPrime(t)):
#     print("Prime")
# else:
#     print("Not ")


t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    for j in range(1,100):
        s=x+y+j
        if(isPrime(s)):
            print(j)
            break
