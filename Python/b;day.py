from datetime import datetime
import time
import sys


def timed():
    d = input("Enter your birth date: ")
    o = input("Enter your birth month:")
    b = input("Enter your birth year: ")
    print("Entered D.O.B is {}\\{}\\{}".format(d,o,b))
    # dob = input("Enter DOB, use dd mm yyyy format: ")
    dob = datetime.strptime(dob , '%d %m %Y')
    print("Here are your age statistics...")
    time.sleep(0)
    print("Years : %d" % ((datetime.today() - dob).days / 365))
    print("Months : %d" % ((datetime.today() - dob).days / 30.4))
    print("Weeks : %d" % ((datetime.today() - dob).days / 7))
    print("Days: %d" % ((datetime.today() - dob).days))
    print("Hours : %d" % ((datetime.today() - dob).days * 24))
    print("Minutes : %d" % ((datetime.today() - dob).days * 1440))
    print("Seconds : %d" % ((datetime.today() - dob).days * 86400))
    month()
    p = int(input("Enter 1 for calculating another age statistics \nenter 2 to exit "))
    if p == 1:
        repeat()
    else:
        ex()


def ex():
    print("Thanks for giving your precious time")
    sys.exit()


def repeat():
    timed()


def month():
    import datetime
    print("Month of year : ", datetime.date.today().strftime(("%m")))


# def date_ofb():


# def age_month():

timed()

'''import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime(("%m")))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))'''
