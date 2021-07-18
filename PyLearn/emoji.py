win=69
n=int(input("Guess a number: "))
num=0
while(num==0):
    if(n==win):
        print("Bingo!!!")
        break
    elif(n<win):
        print("Num is too small")
    else:
        print("Num is too big")

