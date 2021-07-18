# def sequences(arr, index, subarr):
#     if index == len(arr):
#         if len(subarr) != 0:
#             # print(subarr)
#             li.append(subarr)
#     else:
#         sequences(arr, index + 1, subarr)
#         sequences(arr, index + 1, subarr + [arr[index]])
#     return
#
# def most_frequent(lis):
#     counter = 0
#     num = lis[0]
#     for j in lis:
#         frequency = lis.count(j)
#         if frequency > counter:
#             counter = frequency
#             num = j
#     return num % (10 ** 9 + 7)
#
#
# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     li = []
#     li1 = []
#     li2 = []
#     sequences(arr, 0, [])
#     # print(li)
#     if len(li) == 1:
#         li1.append(li[0])
#     else:
#         for i in li:
#             li1.append(most_frequent(i))
#     # print(li1)
#     for i in range(1, n+1):
#         # li2.append(li1.count(i))
#         li2.append(li1.count(i) % (10 ** 9 + 7) )
#     print(*li2)


def sequences(arr, index, subarr):
    if index == len(arr):
        if len(subarr) != 0:
            # print(subarr)
            li.append(subarr)
    else:
        sequences(arr, index + 1, subarr)
        sequences(arr, index + 1, subarr + [arr[index]])
    return

def most_frequent(lis):
    counter = 0
    num = lis[0]
    for j in lis:
        frequency = lis.count(j)
        if frequency > counter:
            counter = frequency
            num = j
    return num


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    li = []
    li1 = []
    li2 = []
    sequences(arr, 0, [])
    # print(li)
    for i in li:
        li1.append(most_frequent(i))
    # print(li1)
    for i in range(1, n+1):
        # li2.append(li1.count(i))
        li2.append(li1.count(i))
    print(*li2)



# def sub_lists(list1):
#     sublist = [[]]
#     for x in range(len(list1) + 1):
#         for j in range(x + 1, len(list1) + 1):
#             sub = list1[x:j]
#             sublist.append(sub)
#     return sublist
#
# def most_frequent(lis):
#     counter = 0
#     num = lis[0]
#     for j in lis:
#         frequency = lis.count(j)
#         if frequency > counter:
#             counter = frequency
#             num = j
#     return num
#
#
# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     # li = []
#     li1 = []
#     li2 = []
#     li = sub_lists(arr)
#     print(li)
#     for i in li:
#         if len(i) == 0:
#             li.remove(i)
#         elif len(i) == 1:
#             li1.append(li[0][0])
    # print(li)
    # print(li1)
    # for i in li:
    #   li1.append(most_frequent(i))
    # print(li1)
    # for i in range(1, n+1):
    #     # li2.append(li1.count(i))
    #     li2.append(li1.count(i))
    # print(*li2)