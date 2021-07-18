lis=[]
le=int(input("Enter the size of list:"))
for i in range(le):
    x=int(input("Enter the element to be inserted in list:"))
    lis.append(x)

def eo(lis):
    even = 0
    odd = 0
    for i in lis:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

eve,od=eo(lis)

print("Num of evens are {0} & num of odds are {1}".format(eve,od))