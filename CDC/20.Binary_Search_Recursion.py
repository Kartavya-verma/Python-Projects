def binary(l,find_num,s,e):
    if e >= s:
        mid = (e + s) // 2
        if l[mid] == find_num:
            return mid
        elif l[mid] > find_num:
            return binary(l,find_num,s,mid-1)
        elif l[mid] < find_num:
            return binary(l,find_num,mid+1,e)
    else:
        return -1


l = list(map(int,input().split()))
find_num = int(input())
res = binary(l,find_num,0,len(l)-1)
if res != -1:
    print("Element Present at index:",res)
else:
    print("Element is not present")