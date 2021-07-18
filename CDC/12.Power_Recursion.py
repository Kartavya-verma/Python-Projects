def pow(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    else:
        return base * pow(base, power-1)


base, power = map(int,input().split())
print(pow(base,power))