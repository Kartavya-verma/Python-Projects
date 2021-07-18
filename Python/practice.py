'''for i in range(1,11):
    if i==5:
        continue
    else:
        print("Hello KV",i)'''

'''import array as arr

val=arr.array('i',[5,9,1,4,10])
print(val)
print(type(val))'''

from array import *
arr=array('i',[])
n=int(input("Enter the length of array: "))
for i in range(n):
    x=int(input("Enter the value:"))
    arr.append(x)
