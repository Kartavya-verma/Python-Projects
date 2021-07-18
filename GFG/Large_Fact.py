def fact(i):
    if i == 0 or i == 1:
        return 1
    else:
        return (i * fact(i-1)) % 1000000007


# n = int(input())
# l = list(map(input().split()))
l = [0,1,2,3,4]
res = []
for i in l:
    res.append(fact(i))
print(res)



# t = []
# mod = 1000000007
# SIZE = 10000
# fact = [1]*SIZE
# for i in range(1,SIZE):
#     fact[i] = (fact[i-1]*i) % mod
# for i in a:
#     t.append(fact[i])
# return t
