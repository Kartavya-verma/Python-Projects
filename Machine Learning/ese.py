# def check(s, m):
#     l = len(s)
#     c1 = 0
#     c2 = 0
#     for i in range(0, l - 1):
#         if s[i] == '0':
#             c2 = 0
#             c1 = c1 + 1
#         else:
#             c1 = 0
#             c2 = c2 + 1
#         if c1 == m or c2 == m:
#             return True
#     return False
#
#
# # Driver Code
# s = input()
# m = 3
#
# if check(s, m):
#     print("Accepted")
# else:
#     print("Rejected")

st = input("Enter a String:")
print("Accepted") if st.count("0") == st.count("1") else print("Rejected")
