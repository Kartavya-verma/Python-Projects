# def encode(s):
#     if s == "0000":
#         return "a"
#     elif s == "0001":
#         return "b"
#     elif s == "0010":
#         return"c"
#     elif s == "0011":
#         return "d"
#     elif s == "0100":
#         return "e"
#     elif s == "0101":
#         return "f"
#     elif s == "0110":
#         return "g"
#     elif s == "0111":
#         return "h"
#     elif s == "1000":
#         return "i"
#     elif s == "1001":
#         return "j"
#     elif s == "1010":
#         return "k"
#     elif s == "1011":
#         return "l"
#     elif s == "1100":
#         return "m"
#     elif s == "1101":
#         return "n"
#     elif s == "1110":
#         return "o"
#     elif s == "1111":
#         return "p"
#
#
# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     if len(s) == 4:
#         print(encode(s))
#     else:
#         s1 = s[:len(s) // 2]
#         s2 = s[len(s) // 2:]
#         print(encode(s1) + encode(s2) )


# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     g = "abcdefghijklmnop"
#     z = 0
#     o = 0
#     for i in s:
#         if i == "0":
#             z += 1
#             if z == 1:
#                 print("1",g[:len(g)//2])
#             elif z == 2:
#                 print("2",g[:len(g) // 4])
#             elif z == 3:
#                 print("3",g[:len(g) // 8])
#             elif z == 4:
#                 print("4",g[:len(g)//16])

for _ in range(int(input())):
    n = int(input())
    s = input()
    r = ""
    # d = {"0000":"a","0001":"b","0010":"c","0011":"d","0100":"e","0101":"f","0110":"g","0111":"h","1000":"i","1001":"j","1010":"k","1011":"l","1100":"m","1101":"n","1110":"o","1111":"p"}
    d = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p"}
    for i in range(0, len(s), 4):
        r += d[int(s[i:i+4], 2)]
    print(r)
    # if n == 4:
    #     # if s in d.keys():
    #     print(d[s])
    # else:
    #     if s[:len(s)//2] and s[len(s)//2:] in d:
    #         print(d[s[:len(s)//2]] + d[s[len(s)//2:]])

# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     b = int(s, 2)
#     print(b)
#     res = ""
#     while b > 0:
#         c = chr(ord('a') + (b-1) % 16)
#         res = c + res
#         b = (b-1) // 16
#     print(res)

