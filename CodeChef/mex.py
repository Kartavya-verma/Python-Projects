li=list(map(int,input().split()))
li1=[]
li2=[]
for i in li:
    i=str(i)
    li1.append(eval(i))
# print(li)
# print(li1)
a=set(li)
b=set(li1)
print(a.symmetric_difference(b))
print(li2)