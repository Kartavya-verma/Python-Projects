def fib(x):
    if x==0 or x==1:
        return 0
    else:
        return(fib(x)+fib(x-1))


a=int(input("Enter a num: "))
for i in range(0,50,1):
        re=fib(i)
        print(re)
