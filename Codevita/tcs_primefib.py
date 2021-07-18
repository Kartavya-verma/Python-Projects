numbers = input().split()
no1 = int(numbers[0])
no2 = int(numbers[1])
prime = []
for num in range(no1, no2 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime.append(num)
pair = []
for i in range(len(prime)):
    for j in range(len(prime)):
        if (i != j):
            pair.append(int(str(prime[i]) + str(prime[j])))
prime1 = []
for num in pair:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime1.append(i + 1)
prime1.sort()
min = prime1[0]
max = prime1[-1]
prime1=(list(set(prime1)))
if len(prime1) == 1:
    print(min)
else:
    for i in range(len(prime1)):
        if (i == (len(prime1)-1)):
            print(min)
        temp = min + max
        min = max
        max = temp