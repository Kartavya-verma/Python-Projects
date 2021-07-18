L = 1
R = 100
p1 = []
for i in range(2,int(R**0.5)+1):
    if i<=3:
        p1.append(i)
    else:
        for j in range(5,int(i**0.5)+1,6):
            if i%j==0 or i%(j+2)==0:
                break
        p1.append(i)
# print(p1)

d = {}
for i in range(L, R + 1):
    d[i] = 0
# print(d)
# print(len(d))

for i in p1:
    for p2 in d.keys():
        # print(p2, i)
        if p2 % i == 0 and p2 != i:
            # print(p2)
            d[p2] = 1
# print(d)
for key, value in d.items():
    if value == 0:
        print(key)