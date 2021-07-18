numbers=list(range(1,11))

def square(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square

print(square(numbers))