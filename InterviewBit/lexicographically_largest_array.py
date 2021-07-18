a = list(map(int, input().split()))
# print(sorted(a))
# if a == sorted(a):
#     print(a[::-1])
# else:

# max_index = a.index(max(a))
# min_index = a.index(min(a))
# x = a[]
#
#
# x = a[max_index:]
# # print(x)
# y = a[max_index + 1:]
# x.extend(y[::-1])
# print(x)
# # print(y)




# if a == sorted(a):
#     print(a[::-1])
# else:
#     max_index = a.index(max(a))
#     min_index = a.index((min(a)))
#     if max_index == 0:
#         x = a[0:max_index + 1]
#         y = a[max_index + 1:]
#         x.extend(y[::-1])
#         print(x)
#     elif min_index == len(a)-1:
#         print(a)
#     elif max_index == len(a)-1:
#         print(a[::-1])
#     elif min_index == 0:
#         print(a[::-1])



i, j = 0, len(a) -1
x, y = [], []
while i < j:
    if a[i] <= a[j]:
        y.append(a[i])
        j -= 1
    else:
        x.append(a[i])
        i += 1
print(x)
print(y)






# i, j = 0, len(a) - 1
# while i < j:
#     if a[i] > a[j]:
#         j -= 1
#     else:
#         i += 1
# x = a[:i+1]
# # print(x)
# y = a[j:]
# # print(y)
# y = y[::-1]
# # print(x)
# # print(y)
# x.extend(y)
# print(x)
# print(y)
# # print(x)