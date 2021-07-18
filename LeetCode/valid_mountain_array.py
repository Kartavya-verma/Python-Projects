# arr = [0,3,2,1]
# i = 0
# while i < len(arr) and i+1 < len(arr) and arr[i] < arr[i+1]:
#     i += 1
# if i == 0 or i + 1 >= len(arr):
#     print("False")
# while i < len(arr) and i + 1 < len(arr):
#     if arr[i] <= arr[i+1]:
#         print("False")
# print("True")

A = [0,3,2,1]
if len(A) < 3 or A[0] >= A[1]:
    print("False")
increase = True
for i in range(1, len(A)):
    if A[i-1] > A[i]:
        increase = False
    if not increase and A[i-1] < A[i]:
        print("False")
    if A[i-1] == A[i]:
        print("False")
print(not increase)