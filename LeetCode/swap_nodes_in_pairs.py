n = 5
tri = [[1] * i for i in range(1, n + 1)]
i = 1
while i < n:
    for j in range(1, len(tri[i-1])):
        # print("i=", i, "j=", j)
        # print("tri[i][j] = ", tri[i][j], "tri[i-1][j] = ", tri[i-1][j], "tri[i-1][j-1]", tri[i-1][j-1])
        tri[i][j] = tri[i-1][j] + tri[i-1][j-1]
        # print("tri[i][j] = ", tri[i][j])
    i += 1
print(tri)
# print(len(tri[5]))