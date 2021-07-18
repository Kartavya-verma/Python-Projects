# class Solution:
#     def myAtoi(self, s: str) -> int:
#         res=""
#         for i in range(len(s)):
#             if s[i]!=" " and s[i]!="+" and s[i]!="-" and not s[i].isdigit():
#                 break
#             elif s[i]=="+" or s[i]=="-" or s[i].isdigit():
#                 res+=s[i]
#                 j = i+1
#                 while j<len(s) and s[j].isdigit():
#                     res+=s[j]
#                     j+=1
#                 break
#         if res=="" or res=="+" or res=="-":
#             return 0
#         elif int(res)>2147483647:
#             return 2147483647
#         elif int(res)<-2147483648:
#             return -2147483648
#         else:
#             return int(res)
#
#
# str = "      -42"
# str = str.strip()
# res = ""
# print(str)
#
# if not str:
#     print(0)
#
# if str[0] == "-":
#     neg = True
# else:
#     neg = False
#
# for i in range(len(str)):
#     if str[i] == "+" or str[i].isnumeric():
#         res += str[i]
#
#
# if neg:
#     res = -1 * res
# print(res)

str = "    -42"
if len(str) == 0:
    print(0)
ls = list(str.strip())

if ls[0] == '-':
    sign = -1
else:
    sign = 1

if ls[0] in ['-', '+']:
     ls.pop(0)

res, i = 0, 0
while i < len(ls) and ls[i].isdigit():
    res = res * 10 + ord(ls[i]) - ord('0')
    i += 1
print(max(-2 ** 31, min(sign * res, 2 ** 31 - 1)))