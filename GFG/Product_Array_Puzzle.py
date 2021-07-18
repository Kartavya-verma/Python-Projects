def product(nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(0, n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n - 1, -1, -1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output


li = list(map(int,input().split()))
print(product(li))




# l = []
# r = []
# sl = 1
# sr = 1
# for i in range(len(li)):
#     sl *= li[i]
#     l.append(sl)
# for i in range(len(li)-1,-1,-1):
#     sr *= li[i]
#     r.append(sr)
# r.reverse()
# print(sl,sr)
# print(l,r)
# res = []
# res.append(r[0])
# for i in range(1,len(l)-1):
#     res.append(l[i-1]*r[i+1])
# res.append(l[len(l)-2])
# print(res)




