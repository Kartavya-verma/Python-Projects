import datetime



def findAge(current_date, current_month, current_year, birth_date, birth_month, birth_year):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (birth_date > current_date):
        current_month = current_month - 1
        current_date = current_date + month[birth_month - 1]

    if (birth_month > current_month):
        current_year = current_year - 1
        current_month = current_month + 12
        calculated_date = current_date - birth_date
        calculated_month = current_month - birth_month
        calculated_year = current_year - birth_year
        print("Present Age")
        print("Years:", calculated_year, "Months:", calculated_month, "Days:", calculated_date)
    #return int(current_date, current_month, current_year, birth_date, birth_month, birth_year)
    # driver code


current_date = str(print("Current date and time: ", datetime.datetime.now()))
current_year = str(print("Current year: ", datetime.date.today().strftime("%Y")))
current_month = str(print("Month of year: ", datetime.date.today().strftime(("%m"))))

# birth dd//mm//yyyy
birth_date = str(input("Enter your birth date: "))
birth_month = str(input("Enter your birth month "))
birth_year = str(input("Enter your birth year: "))

findAge(current_date, current_month, current_year, birth_date, birth_month, birth_year)

