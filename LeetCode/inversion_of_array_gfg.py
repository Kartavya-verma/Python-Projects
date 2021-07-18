def inversionCount(a,n):
    # Your Code Here
    if len(set(a)) == 1 or sorted(a) == a:
        return 0
    else:
        t = 0
        for i in range(n):
            for j in range(i,n):
                print(a[i], a[j])
                if a[i] > a[j]:
                    t += 1
                    print(t)
    return t


# a = [2,4,1,3,5]
a = [10,10,10]
a = [2,3,4,5,6]
print(inversionCount(a,len(a)))