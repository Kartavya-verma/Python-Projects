nums = [1, 3, 4, 2, 2]
# nums = [3, 1, 3, 4, 2]
dic = {}
for i in nums:
    if i not in dic:
        dic[i] = nums.count(i)
# print(dic[max(dic.values())])
v = max(dic.values())
for i in dic:
    if dic[i] == v:
        print(i)