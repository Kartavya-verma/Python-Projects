n, m = map(int, input().split())
res = []
for _ in range(n):
    a, b = map(int, input().split())
    p = m * (a/b)
    res.append(p)
print(min(res))