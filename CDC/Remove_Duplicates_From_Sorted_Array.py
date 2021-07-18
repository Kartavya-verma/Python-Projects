l = [1,2,2,3,4,4,4,5,5]
for i in range(len(l)):
    if l[i] != l[l[i]-1]:
        temp = l[l[i]-1]
        l[l[i] - 1] = l[i]
        l[i] = temp
print(l)
j = 0
for j in range(len(l)):
    if l[j] != j+1:
        break
print(j)