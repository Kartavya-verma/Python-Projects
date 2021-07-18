# for _ in range(int(input())):
#     c, d, l = map(int, input().split())
#     tot = (c + d) * 4
#     if tot % l == 0 and l >= 4:
#         print("yes")
#     else:
#         print("no")

from sys import stdin, stdout
int_input = lambda: int(stdin.readline().strip())
int_list = lambda: list(map(int, stdin.readline().strip().split()))
for _ in range(int_input()):
    c, d, legs = int_list()
    if legs % 4 == 0 and legs <= (c + d) * 4 and legs >= d * 4 + max(c - 2 * d, 0) * 4:
        stdout.write('yes\n')
    else:
        stdout.write('no\n')