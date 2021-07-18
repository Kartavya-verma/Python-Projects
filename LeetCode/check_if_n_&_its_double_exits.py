arr = [-2,0,10,-19,4,6,-8]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] == arr[j] * 2 and i != j:
            print("True")
print("False")