# l=[3,5,7]
# li=[6,5,10]
l=[3]
li=[7]
for i in l:
    if(i==li[0]):
        print("same")
    elif(i<li[0]):
        if(li[0]%i==0):
            print("mul",li[0]/i)
        else:
            print("add",li[0]-i)

    elif(i>li[0]):
        pass
