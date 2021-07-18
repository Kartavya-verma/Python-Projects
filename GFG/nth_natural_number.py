def natural(n):
    res = 0
    temp = 1
    while n > 0:
        res = res + temp*(n%2)
        n = n//2
        temp = temp * 10
        print(res,n,temp)
    return res


n = int(input())
print(natural(n))