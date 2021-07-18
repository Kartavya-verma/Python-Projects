'''lis=[]
n=int(input("Enter the length of list: "))
for i in range(n):
    a=int(input("Enter the value to be inserted in list:"))
    lis.append(a)
for i in lis:
    print(i,end=" ")'''

from array import *

array=array('i',[])
num=int(input("Enter the length of array: "))
for i in range(num):
    x=int(input("Enter the element to be inserted in array: "))
    array.append(x)
for i in array:
    print(i,end=" ")