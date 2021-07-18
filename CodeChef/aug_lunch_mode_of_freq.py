for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    # print(freq)
    lis = []
    for i in freq:
        lis.append(freq[i])
    # print(lis)
    freq1 = {}
    for item in lis:
        if item in freq1:
            freq1[item] += 1
        else:
            freq1[item] = 1
    print(freq1)
    lis = []
    all_values = freq1.values()
    for j in all_values:
        lis.append(j)
    if len(set(lis)) == 1:

    # print(max(all_values))








    # if all(j == freq1[j] for j in freq1.values()):
    #     minkey = min(freq1, key=freq1.get)
    #     print(minkey)
    # else:
    #     all_values = freq1.values()
    #     max_value = max(all_values)
    #     print(freq1[max_value])



# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     s = set(arr)
#     lis = []
#     for i in s:
#         lis.append(arr.count(i))
#     # print(lis)
#     s1 = set(lis)
#     lis1 = []
#     for j in s1:
#         lis1.append(lis.count(j))
#     # print(lis1)
#     # for i, j in zip(list(set(lis)), lis1):
#     print(max(j for i, j in zip(list(set(lis)), lis1)))