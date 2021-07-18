# def CountFrequency(my_list):
#     count = {}
#     for i in my_list:
#         count[i] = count.get(i, 0) + 1
#     count=list(count.values())
#     return count

# def duplicates(listOfElems):
    # if len(listOfElems) == len(set(listOfElems)):
    #     return False
    # else:
    #     return True

t=int(input())
for x in range(t):
    n=int(input())
    my_list=list(map(int,input().split()))
    my_list.sort()
    print(my_list)
    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    count = list(count.values())
    if 1 in count:
        if len(count) == len(set(count)):
            print("YES")
        else:
            print("NO")



