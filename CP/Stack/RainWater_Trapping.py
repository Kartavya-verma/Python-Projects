arr = [0,1,0,2,1,0,1,3,2,1,2,1]
mxl = [0] * len(arr)
mxr = [0] * len(arr)
water = [0] * len(arr)

mxl[0] = arr[0]
mxr[-1] = arr[-1]

for i in range(1, len(arr)):
    mxl[i] = max(mxl[i-1],arr[i])

for i in range(len(arr)-2,-1,-1):
    mxr[i] = max(mxr[i+1], arr[i])

for i in range(len(arr)):
    water[i] = min(mxl[i],mxr[i]) - arr[i]

# print(mxl,mxr,water)
print(sum(water))