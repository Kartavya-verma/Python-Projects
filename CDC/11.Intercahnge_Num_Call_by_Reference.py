def interchange(a, b):
    a = a+b
    b = a-b
    a = a-b
    return a,b


a, b = map(int,input().split())
print(interchange(a,b))