'''name=input("Enter a name:")

if name==name[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")'''

def char(a):
    if a==a[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
    return a
name=input("Enter a name:")
char(name)