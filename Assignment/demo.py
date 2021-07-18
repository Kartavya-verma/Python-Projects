x=int(input())
l=[]
for i in range(x):
    l.append([input(),float(input())])
print(l)

for i in range(x):
    temp=max(l[i][1])
    print(temp)
'''[['Harry', 37.21], 
 ['Berry', 37.21], 
 ['Tina', 37.2],
 ['Akriti', 41], 
 ['Harsh', 39]
]'''