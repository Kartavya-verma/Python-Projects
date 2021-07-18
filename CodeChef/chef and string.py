t=int(input())
for i in range(t):
    s=input()
    c=0
    c+=s.count('xy')
    s=s.replace('xy',"")
    c+=s.count('yx')
    print(c)