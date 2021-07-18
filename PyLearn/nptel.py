'''import random
def get_gate():
    r=random.randint(0,2)
    r1= random.randint(0, 2)
    while(r==r1):
        r = random.randint(0,2)
    l=['x','x','x']
    l[r]='c'
    l[r1]='c'
    ind=[0,1,2]
    for each in ind:
        if(each!=r1 and each!=r):
            l[each]='g'
    print(l)
get_gate()

import random
while(1):
    r = random.randint(0, 1)
    if(r==0):
        print('tossing')
        break
    else:
        print('tossing')

import random
p1=["rock","paper","scissor"]
p2=["rock","paper","scissor"]
c1=random.choice(p1)
c2=random.choice(p2)
if(c1==c2):
    print("SUCCESS")
else:
    print("FAIL")

t=[]
for i in range(10):
    a=int(input("Enter the number you want to insert in the list"))
    print(i)
    if(len(t)==0):
        t.append(a)
    else:
        if(a>t[len(t)-1]):
            t.append(a)
print(t)

import random
bins={}
for i in range(1,11):
    bins[i]=0
for i in range(1,101):
    r=random.randint(1,10)
    bins[r]=bins[r]+1
print(bins)

min_=0
min_i=-1
for each in bins:
    if(bins[each]>min_):
        min_i=each
        min_=bins[each]
print(min_i)

def mbin():
    max_=0
    max_i=-1
    for each in bins:
        if(bins[each]>max_):
            max_i=each
            max_=bins[each]
        print(max_i)
        return max_i
while(len(bins)>0):
    b=mbin()
    del(bins[b])

def find(list1,num):
    for each in list1:
        if(each!=num):
            print(each)
        else:
            break
t=[]
for i in range(100000):
    t.append(i)
find(t,99999)

import random
while(1):
    r=random.randint(1,6)
    if(r%2==0):
        print('rolling')
        break
    else:
        print('rolling')'''

import random
bins={}
for i in range(1,11):
    bins[i]=0
for i in range(1,101):
    r=random.randint(1,10)
    bins[r]=bins[r]+1
print(bins)

import matplotlib.pyplot as plt
val=bins.values()
x=[]
y=[]
print(val)
for each in list(set(val)):
    x.append(each)
    y.append(val.count(each))
    print(each,val.count(each))
plt.plot(x,y)
plt.show()
