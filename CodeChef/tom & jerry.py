t=int(input())
for i in range(t):
    ts=int(input())
    s=[j for j in range(ts) if j%2==0 and j!=0]
    # print(len(s))
    for k in range(len(s)):
