# minutes alive calculator
def minutesalive(age_years):
    DAYS_IN_YEAR = 365.25
    DAYS_IN_HOURS = 24
    DAYS_IN_MINUTES = 60

    TOTAL_DAYS = DAYS_IN_YEAR*age_years
    TOTAL_HOURS =TOTAL_DAYS*DAYS_IN_HOURS
    TOTAL_MINUTES = TOTAL_HOURS*DAYS_IN_MINUTES

    return round(TOTAL_DAYS),round(TOTAL_HOURS),round(TOTAL_MINUTES)

while True:
    try:
        age=float(input("enter your age in years: "))
        # unpacking of tuples, here minutesalive function  have three values 
        # these values round(TOTAL_DAYS),round(TOTAL_HOURS),round(TOTAL_MINUTES) are stored in minutesalive function 
        # by writting in this manner  days,hours,minutes = minutesalive(age)
        # first value goes to days and the second one goes to hours and the third one goes to the minutes 

        days,hours,minutes = minutesalive(age)

        print("\n You are Approx:")
        print(f"{days} days old ")
        print(f"{hours} hours  old ")
        print(f"{minutes} minutes old ")

        again = input("Would you like to try again? (y/n)").strip().lower()

        if again!= 'y':
            print("Good bye!")
            break
    except:
        print("Please enter a valid number for age: ")
#  Features of try and except:

# Error prevention from crashing

# Without try/except, if an error happens, Python stops the program with a traceback.

# With try/except, you can catch the error and decide what to do next.