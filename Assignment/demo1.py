n=int(input())
l=[]
for i in range(n):
    l.append([input(),float(input())])

marks=list(set(i[1] for i in l))
marks.sort()

l=[i[0] for i in l if(i[1]==marks[1]) ]
l.sort()
