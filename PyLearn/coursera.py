l= []
n = int(input())
for i in range(0, n):
    ele = int(input())
    l.append(ele)  # adding the element
print(l)

n=len(l)
total=int((n+1)*(n+2)/2)
#print(total)
miss=total-sum(l)
print(miss)