from math import factorial
for i in range(int(input())):
    n = int(input())
    if factorial(n)%10 == 0:
        print("Divisible")
    else:
        print("Not Divisible")