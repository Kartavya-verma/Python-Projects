a = 2
b = 5
a, b = b, a
print(a)

for i in range(10):
    print(i)

k = 10
while (k <= 20):
    print(k)
    k += 1

import random

print(random.randrange(1, 10))  # 1,10 excluded

print(random.random())  # between 0-1

print(random.randint(1, 5))  # 1,5 included

l = []
l.append(2)
print(l)

l.append(3)
l.append(0)
l.reverse()
print(l)

l.sort()
print(l)
l.insert(0, 9)
l.pop()
# l.min()
# l.max()
# l.sum()

del l[-1]
print(l)

cubes = []
for x in [1, 2, 3, 4, 5]:
    cubes.append(x ** 3)
print(cubes)

cube = [i ** 3 for i in [1, 2, 3, 4, 5]]
print(cube)

# n = int(input("Enter any number"))
# number = []
# for i in range(n):
#    num = int(input("Enter list of numbers:"))
#   number.append(num)
# print(number)
# for i in number:
#    print(i)
#    if i%2 != 0:
#        print(number,i)
#       number.remove(i)
#       print(number,i)
# print(number)

d = {'a': 25, 'b': 35, 'c': 56}
print(d)

# print(d.has_key(b))

d1 = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(d1)

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5, 6])  # y values and x values are taken automatically of indices
plt.show()

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.show()

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'r')  # red colour line
plt.show()

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro')
plt.show()

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro-')
plt.show()

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'r^-')
plt.show()

plt.title('Squares of the numbers')
plt.xlabel('The Numbers')
plt.ylabel('The squares')
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro')
plt.show()

plt.title('Squares of the numbers')
plt.xlabel('The Numbers', fontsize=18, color='red')
plt.ylabel('The squares')
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro')
plt.show()

plt.title('Squares of the numbers')
plt.xlabel('The Numbers', fontsize=18, color='red')
plt.ylabel('The squares')
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro', linewidth=3.0)
plt.show()

plt.grid(True)
plt.title('Squares of the numbers')
plt.xlabel('The Numbers', fontsize=18, color='red')
plt.ylabel('The squares')
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro-', linewidth=3.0)
plt.show()