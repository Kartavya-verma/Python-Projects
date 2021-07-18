# for i in range(int(input())):
#     n, m, k = [int(x) for x in input().split()]
#     m1 = list(map(int, input().split()))
#     k1 = list(map(int, input().split()))
#     ans = []
#     ans.append(len(set(m1).intersection(k1)))
#     m1.extend(k1)
#     ans.append(len(set(range(1, max(m1)+1))-set(m1).union(k1)))
#     print(*ans)

for i in range(int(input())):
    n, m, k = [int(x) for x in input().split()]
    m1 = set(map(int, input().split()))
    k1 = set(map(int, input().split()))
    print(len(m1.intersection(k1)), n - len(m1.union(k1)))

