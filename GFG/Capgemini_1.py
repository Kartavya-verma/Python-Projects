def count(a,b,m,n):
    if (m == 0 and n == 0) or n == 0:
        return 1
    if m == 0:
        return 0
    if a[m-1] == b[n-1]:
        return count(a,b,m-1,n-1) + count(a,b,m-1,n)
    else:
        return count(a,b,m-1,n)

a = "MOM"
b = "DAD"
st = input()
ans = count(st,a,len(st),len(a)) + count(st,b,len(st),len(b))
print(ans)