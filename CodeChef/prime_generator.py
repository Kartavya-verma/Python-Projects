# cook your dish here
def isPrime(n):
    if n<=1: return False
    if n<=3: return True
    if (n%2==0 or n%3==0): return False

    # i = 5
    # while(i < int(n ** 0.5) + 1):
    #     if n%i==0 or n%(i+2)==0:
    #         return False
    #     i+=6
    # return True

    for i in range(5, int(n ** 0.5)+1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

for _ in range(int(input())):
    m,n = map(int,input().split())
    for k in range(m,n+1):
        if isPrime(k):
            print(k)
    print() 