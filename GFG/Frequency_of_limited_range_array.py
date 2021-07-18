def frequency(l,n):
    for i in range(n):
        l[i] -= 1
    print(l)
    for i in range(n):
        l[l[i]%n] += n
    print(l)
    for i in range(n):
        l[i] = l[i]//p
    return l


n = int(input())
l = list(map(input().split()))
print(frequency(l,n))