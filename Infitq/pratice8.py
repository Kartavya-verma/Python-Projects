s = list(map(int, input().split(",")))
print(s)
f = s.index(4)
se = s.index(7)
su = s[:f]
seve = s[se+1:]
res = sum(su)+sum(seve)
print(res)
bet = s[f:se+1]
c = ''
for i in bet:
    c += str(i)
print(int(c)+res)
