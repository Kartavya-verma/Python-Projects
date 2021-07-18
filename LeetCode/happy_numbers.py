n = 19


def sqsum(num):
    result = 0
    while num > 0:
        r = num % 10
        result = result + r * r
        num = num // 10
    return result


seen = set()
while sqsum(n) not in seen:
    sum1 = sqsum(n)
    if sum1 == 1:
        print("True")
    else:
        seen.add(sum1)
        n = sum1
print("False")