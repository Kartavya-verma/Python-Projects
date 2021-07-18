# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(len(set(a)) - 1) if 0 in a else print(len(set(a)))

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(len(set(a)) - 1)
    else:
        print(len(set(a)))