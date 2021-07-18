def ls(l,find_num,s,e):
    if e < s:
        return -1
    if l[s] == find_num:
        return s
    if l[e] == find_num:
        return e
    return ls(l,find_num,s+1,e-1)


l = list(map(int,input().split()))
find_num = int(input())
res = ls(l,find_num,0,len(l)-1)
if res != -1:
    print("Element Present at index:",res)
else:
    print("Element is not present")