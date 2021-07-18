su = 44
arr = [46,22, 14, 97, 22, 67, 30, 95, 23, 30, 6, 17, 40, 69, 60, 97, 70, 66, 45, 32, 13, 4, 74, 40, 61, 49, 2 ,23, 96, 55, 17, 93, 28, 30, 41, 2 ,96, 70, 96, 18, 51, 53, 86]
f = 0
dic = {}
for i in arr:
    dic[i] = arr.count(i)
for j in arr:
    if su - j in dic:
        f += dic[su-j]
print(f//2)
print(f/2)