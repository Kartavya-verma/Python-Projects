def digitsInFactorial(N):
    # code here
    f = 1
    for i in range(1, N + 1):
        f = f * i
    return len(str(f))

print(digitsInFactorial(120))