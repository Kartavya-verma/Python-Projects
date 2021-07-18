from math import ceil
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    c = 0
    for i in l:
        if i != -1:
            c += 1
    if c < ceil(n/2):
        print("Rejected")
    else:
        for i in l:
            if i == 0:
                l.remove(i)
        if any(elem > k for elem in l):
            print("Too Slow")
        elif all(elem == l[0] for elem in l):
            print("Bot")
        else:
            print("Accepted")

# //////////
    n, k = map(int, input().split())
    l = list(map(int, input().split()))

    bot = 1
    correct = 0
    slow = 0

    for x in l:
        if (x not in [0, 1]):
            bot = 0
        if (x != -1):
            correct += 1
        if (x > k):
            slow = 1

    if (correct < ceil(n / 2)):
        print("Rejected")
    elif (slow == 1):
        print("Too Slow")
    elif (bot == 1):
        print("Bot")
    else:
        print("Accepted")

    # l.remove(0)
    # print(l)
    # for i in l:
    #     if i != 0:
    #         c += 1
    #     else:
    #         l.remove()
    # if c < ceil(n/2):
    #     print("Rejected")
    # else:
    #     if any(l) > k:
    #         print("Too Slow")
    #     elif