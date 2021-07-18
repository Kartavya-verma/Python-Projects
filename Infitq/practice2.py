n = input()
s = [int(n[i:j]) for i in range(len(n)) for j in range(i+1,len(n) +1)]
s = sorted(set(s))
res = []
for num in s:
    for i in range(1,int(num**0.5)+1):
        if (i*(i+1) == num):
            res.append(num)
print(res)