def count(string, substring):
    count = 0
    start = 0
    while start<len(string):
        flag = string.find(substring, start)
        if flag != -1:
            start = flag + 1
            count += 1
        else:
            return count
a=input()
b=input()
print(count(a,b))