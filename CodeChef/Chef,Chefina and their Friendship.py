# t1="ab"
# t2="ab"
# s="abababab"       #t1+t1+t2+t2
# print(s)
# temp=""
# for i in s:
#     temp=i
#     if(temp!=i):

def repeats(string):
    for x in range(1, len(string)):
        substring = string[:x]

        if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
            print(substring)
            return "break"

    print(string)

s="abcd"
repeats(s)




# t=int(input())
# for i in range(t):
#     s=input()     #t1+t1+t2+t2