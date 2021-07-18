# for i in range(int(input())):
#     s=input()
#     freq={}
#     for j in s:
#         if j in freq:
#             freq[j] += 1
#         else:
#             freq[j] = 1
#     print(freq)
#     max_value = max(freq.values())
#     max_key = max(freq,key=freq.get)
#     # print(max_value)
#     # print(max_key)
#     print(freq)
#     summe = 0
#     for l, k in freq.items():
#         if l != max_key and k != max_value:
#             summe = summe + k
#     if summe == max_value:
#         print("YES")
#     else:
#         print("NO")

for j in range(int(input())):
    s=list(input())
    d=len(s)
    f=0
    for i in s:
        if(s.count(i)==d/2):
            f=1
            break
    if(f==1):
        print("YES")
    else:
        print("NO")