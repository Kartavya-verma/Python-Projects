for _ in range(int(input())):
    s = input()
    if s[0].islower() and s[len(s) - 1].islower() and 10 <= len(s) <= 20:
        if any(i.isalnum() for i in s) and any(i.islower() for i in s) and any(i.isupper() for i in s) and any(i in sp for i in s):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")