def wave(l):
    if len(l) % 2 == 0:
        for i in range(0, len(l), 2):
            l[i], l[i + 1] = l[i + 1], l[i]
    else:
        for i in range(0, len(l) - 1, 2):
            l[i], l[i + 1] = l[i + 1], l[i]
    return l


l = [1,2,3,4,5]
print(wave(l))