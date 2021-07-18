arr = [1, 4, 2, 3, 5, 4]
for i in arr:
    if arr.count(i) > 1:
        print(arr.index(i)+1)
        break
    else:
        print(-1)