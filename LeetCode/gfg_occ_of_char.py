s = 'geeksforgeeks'
dic = {}
for i in s:
    if i not in dic:
        dic[i] = s.count(i)
for j in dic:
    print("No.of occurrence of "+j+" is:",dic[j])