n = 47
l = sorted(list(map(int, input().split())))
s = sum(i+1 for i in range(len(l)))
s1 = sum(set(l))
print(sum(l)-s1, s-s1)