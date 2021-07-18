def interchange(a,b):
    temp = a
    a = b
    b = temp
    return a,b


a, b = map(int,input().split())
print(interchange(a,b))