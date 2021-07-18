digits = [4,3,2,1]
# digits = list(int(str(digits)) + 1)
# print(str((digits)))
s = ""
for i in digits:
    s += str(i)
num = int(s) + 1
res = [int(x) for x in str(num)]
print(num)
print(res)