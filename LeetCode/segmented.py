# L = 2
# R = 10
# p1 = []
# for i in range(2,int(R**0.5)+1):
#     if i<=3:
#         p1.append(i)
#     else:
#         for j in range(5,int(i**0.5)+1,6):
#             if i%j==0 or i%(j+2)==0:
#                 break
#         p1.append(i)
# #print(p1)
#
# d = {}
#
# for i in range(L,R+1):
#     d[i]=0
#
# #print(d)
#
# for i in p1:
#     for j in d:
#         if j%i==0 and j!=i:
#             d[j]=1
# for i in d:
#     if d[i]==0:
#         print(i)
#

L = 2
R = 10
p1 = []
for i in range(2,int(R**0.5)+1):
    if i<=3:
        p1.append(i)
    else:
        for j in range(5,int(i**0.5)+1,6):
            if i%j==0 or i%(j+2)==0:
                break
        p1.append(i)
print(p1)

p2 = []
primes = [0]*(R-L+1)

print(primes)

for i in range(L,R+1):
    p2.append(i)
print(p2)

for i in p1:
    for j in range(len(p2)):
        print(p2[j], i)
        if p2[j]%i==0 and p2[j]!=i:
            print(j)
            primes[j]=1
print(primes)
for i in range(len(primes)):
    if primes[i]==0:
        print(p2[i])