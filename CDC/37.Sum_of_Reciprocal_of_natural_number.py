def sum_series(n):
    s = 0
    for i in range(1,n+1):
        s += 1/i
    return s


n = int(input())
print(sum_series(n))