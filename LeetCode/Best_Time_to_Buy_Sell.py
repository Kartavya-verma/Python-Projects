def stock(l):
    mini = float('inf')
    profit = 0
    for i in range(len(l)):
        if l[i] < mini:
            mini = l[i]
        elif l[i] - mini > profit:
            profit = l[i] - mini
    return profit


l = list(map(int,input().split()))
print(stock(l))