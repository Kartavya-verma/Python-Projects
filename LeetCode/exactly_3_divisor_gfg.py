def exactly3Divisors(N):
    # code here
    total = 0
    prime = True
    for i in range(2,int(N ** 0.5) + 1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime = False
                break
        if prime:
            total+=1
        prime = True
    return total
print(exactly3Divisors(67))

#
# def exactly3Divisors(N):
#     # code here
#     total = 0
#     for i in range(2, N + 1):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 break
#         else:
#             if i * i <= N:
#                 total += 1
#                 # print(i)
#     return total
# print(exactly3Divisors(67))


# correct
# def exactly3Divisors(N):
#     # code here
#     total = 0
#     for i in range(2, int(N ** 0.5) + 1):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 break
#         else:
#             if i * i <= N:
#                 total += 1
#     return total
# print(exactly3Divisors(67))
#
#
# correct
# def exactly3Divisors(N):
#     # code here
#     total = 0
#     count = 0
#     for i in range(2, int(N ** 0.5) + 1):
#         for j in range(2, int(i**0.5)+1):
#             if i%j==0:
#                 count = 1
#                 break
#         if count == 0:
#             total += 1
#         count = 0
#     return total
#
# print(exactly3Divisors(67))