#User function Template for python3

#Compelte his function
def termOfGP(A,B,N):
    #Your code here
    n = N - 1
    r = (B / A)
    m = r ** n
    return int(A * m)

print(termOfGP(-27, -78, 3))