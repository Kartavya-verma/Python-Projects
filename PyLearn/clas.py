class Student:
    def __init__(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter age: "))
    def Display(self):
        print("Name of student is {}".format(self.name))
        print("Age of student is {}".format(self.age))

kv=Student()
kv.Display()