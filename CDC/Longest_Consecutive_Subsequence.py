l = [2,6,1,9,4,5,3]
s = set()
for i in l:
    s.add(i)
count = 0
for i in l:
    if i-1 not in s:
        current = i
        current_con = 1
        while current+1 in s:
            current += 1
            current_con += 1
        count = max(current_con,count)
print(count)