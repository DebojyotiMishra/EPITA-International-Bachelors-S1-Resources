### The Date Checker
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
is_month_31 = month==1 or month==3 or month ==5 or month==7 or month==8 or month==10 or month==12
is_month_30 = month==4 or month==6 or month ==9 or month==11

if 1 <= month <= 12:
    if is_month_31 and 1 <= day <= 31:
        print("Valid date") 
    elif is_month_30 and 1 <= day <= 30:
        print("Valid date") 
    elif month == 2:
        if is_leap_year and 1 <= day <= 29:
            print("Valid date") 
        elif not is_leap_year and 1 <= day <= 28:
            print("Valid date")
        else :
            print("Invalid date")
    else :
        print("Invalid date")

### The Car Insurance
age = int(input('Enter your age : '))
lic = int(input('How long ago did you get your license ? (in years) : '))
acc = int(input('Number of accidents : '))
ins = int(input('How many years have you been with this insurance ? : '))

situation = -1

if not(age >= 25) and not(lic >= 2) and acc == 0:
    situation = 3
elif (not(age >= 25) and lic >= 2) or (age >= 25 and not(lic >= 2)) :
    if acc == 0 :
        situation = 2
    elif acc == 1 :
        situation = 3
else :
    if acc == 0 :
        situation = 1
    elif acc == 1 :
        situation = 2
    elif acc == 2 :
        situation = 3

if ins > 5 and situation >= 0 :
    situation -= 1

if situation == 0: package = "Blue"
elif situation == 1: package = "Green"
elif situation == 2: package = "Orange"
elif situation == 3: package = "Red"
else: package = "Refused"

print("Giving your details :",
      "\n\tage :", age, 
      "\n\tlicence existence :", lic,
      "\n\tNumber of accidents :", acc,
      "\n\tSeniority :", ins,
      "\nYour car insurance package is", package)