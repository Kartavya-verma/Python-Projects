def user_info(first_name,last_name,age=23):
    print("Your 1st name is {}".format(first_name))
    print("Your 2nd name is {}".format(last_name))
    print("Your age is {}".format(age))
a,b,c=input("Enter your first name,last name &age: ").split(" ")
user_info(a,b)