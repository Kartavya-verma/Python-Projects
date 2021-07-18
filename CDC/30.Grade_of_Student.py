def grade(m):
    if m >= 60:
        return "First"
    elif 50 <= m < 60:
        return "Second"
    elif 40 <= m < 50:
        return "Third"
    else:
        return "Failed"


m = int(input())
print(grade(m))