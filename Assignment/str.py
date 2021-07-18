import textwrap
s=input()
w=int(input())
my_wrap = textwrap.TextWrapper(width = w)
wrap_list = my_wrap.wrap(text=s)
for i in wrap_list:
    print(i)