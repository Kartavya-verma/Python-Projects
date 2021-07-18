# temp = inp[-1]
# for i in range(len(inp)-1,0,-1):
#     inp[i] = inp[i-1]
# inp[0] = temp
# print(inp)

def reverse(l,s,e):
    while s < e:
        l[s],l[e] = l[e],l[s]
        s += 1
        e -= 1
    return l

l = list(map(int, input().split()))
k = 3
k %= len(l)
for i in range(k):
    l.insert(0,l.pop())
print(l)

# n = k%len(l)
# print(reverse(l,0,len(l)-1))
# print(reverse(l,0,k-1))
# print(reverse(l,k,len(l)-1))