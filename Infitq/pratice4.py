s = input()
l = [str(int(s[i])**2) for i in range(len(s)) if i % 2 != 0]
# l.append()
t = ''.join(i for i in l)
print(t[:4])