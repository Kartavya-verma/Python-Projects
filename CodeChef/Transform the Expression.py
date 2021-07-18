from string import ascii_lowercase
t=int(input())
l=[]
l1=[]
o="+-/*^"
a=ascii_lowercase
for i in range(t):
    s=input()
    for x in s:
        if x in o:
            l.append(x)
        elif x in a:
            l1.append(x)
        elif x==")":
            l1.append(l.pop())
    print("".join(l1))
