n=int(input("Enter a 3 digit number:"))
a=int(n/100)
b=int((n%100)/10)
c=int((n%100)%10)
sum=a+b+c
print("Sum of digits is {}".format(sum))