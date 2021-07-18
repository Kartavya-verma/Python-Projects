m=int(input())
l=[]
for i in input().split():
    l+=[int(i)]
sum1=sum(l)
l=set(l)
sum2=sum(l)
diff = sum2*m-sum1
print(diff//(m-1))