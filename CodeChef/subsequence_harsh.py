def sequences(arr, index, subarr):
    if index == len(arr):
        if len(subarr) != 0:
            #print(subarr)
            li.append(subarr)
    else:
        sequences(arr, index + 1, subarr)
        sequences(arr, index + 1, subarr + [arr[index]])
    return

def most_frequent(lis):
    counter = 0
    num = lis[0]
    for j in lis:
        frequency = lis.count(j)
        if frequency > counter:
            counter = frequency
            num = j
        elif frequency == counter:
            num = min(num ,j)
    return num

p = 1000000007
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    li = []
    li1 = []
    li2 = []
    sequences(arr, 0, [])
    # print(li)
    for i in li:
        li1.append(most_frequent(i))
    # print(li1)
    for i in range(1, n+1):
        # li2.append(li1.count(i))
        li2.append((li1.count(i)) % p)
    print(*li2)