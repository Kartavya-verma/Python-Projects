def fraction(numerator,denominator):
    n, remainder = divmod(abs(numerator), abs(denominator))  # n = quotient
    sign = '-' if numerator * denominator < 0 else ''
    result = [sign + str(n)]
    if remainder == 0:
        return "".join(result)
    result.append(".")
    d = {}
    while remainder != 0:
        if remainder in d:
            result.insert(d[remainder],"(")
            result.append(")")
            break
        d[remainder] = len(result)
        n, remainder = divmod(abs(remainder*10), abs(denominator))
        result.append(str(n))
    return "".join(result)


numerator = int(input())
denominator = int(input())
print(fraction(numerator,denominator))


