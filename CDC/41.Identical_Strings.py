def identical(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True


s1 = input()
s2 = input()
print(identical(s1,s2))