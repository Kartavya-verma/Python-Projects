#string format
'''name=input("Enter your name:")
print("Hello {}".format(name))'''

#string indexing(for)
'''name=input("Enter your name:")
i=0
for i in range(len(name)):
    print("{} index of {} is {}".format(i,name,name[i]))
'''

#string indexing(while)
'''name=input("Enter your name:")
i=0
while i<len(name):
    print("{} index of {} is {}".format(i,name,name[i]))
    i+=1
'''

#String slicing
'''name=input("Enter your name: ")
print(name[-7::])
'''

#Two inputs in one line
name,age=input("Enter your name & age:").split(",")