for _ in range(int(input())):
    q = input()
    if q.count("1") == 0:
        print("Beginner")
    elif q.count("1") == 1:
        print("Junior Developer")
    elif q.count("1") == 2:
        print("Middle Developer")
    elif q.count("1") == 3:
        print("Senior Developer")
    elif q.count("1") == 4:
        print("Hacker")
    elif q.count("1") == 5:
        print("Jeff Dean")