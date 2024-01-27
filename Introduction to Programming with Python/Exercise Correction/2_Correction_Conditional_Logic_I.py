# PALISSON Antoine

### Level - Easy
## Exercise 1-1
number = int(input("Enter a number: "))
if number > 10:
    print("The number is greater than 10.")

## Exercise 1-2
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

## Exercise 1-3
grade = int(input("Enter your grade (0-100): "))
if grade >= 90:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
else:
    print("F")

## Exercise 1-4
a = 5
b = 10
if a < 8 and b > 8:
    print("Both conditions are true.")

## Exercise 1-5
x = 5
if x is 5:  
    print("x is 5.")
# Observation: using 'is' for integer comparison is not recommended in Python

### Level - Moderate
## Exercise 2-1
purchase_amount = float(input("Enter the amount of your purchase: $"))
if 50 < purchase_amount < 100:
    discount = 0.10 * purchase_amount
elif purchase_amount >= 100:
    discount = 0.20 * purchase_amount
else:
    discount = 0
total_amount = purchase_amount - discount
print("Total amount after discount: $", total_amount)

## Exercise 2-2
age = int(input("Enter your age: "))
if age < 12:
    price = 5
elif age < 60:
    price = 10
else:
    price = 7
print("Movie ticket price: $", price)

# Exercise 2-3
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("These sides can form a valid triangle.")
else:
    print("These sides cannot form a valid triangle.")

# Exercise 2-4
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
BMI = weight / (height ** 2)
print("Your BMI is:", BMI)
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI <= 24.9:
    print("You are of normal weight.")
elif 25 <= BMI <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

# Exercise 2-5
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
    print("The result is positive.")
elif num1 == 0 or num2 == 0:
    print("The result is 0.")
else:
    print("The result is negative.")

### Level - Hard
# Exercise 3-1
income = float(input("Enter your income: $"))
tax = 0
if income <= 10000:
    tax = 0.10 * income
elif income <= 40000:
    tax = 0.10 * 10000 + 0.15 * (income - 10000)
elif income <= 80000:
    tax = 0.10 * 10000 + 0.15 * (40000 - 10000) + 0.20 * (income - 40000)
else:
    tax = 0.10 * 10000 + 0.15 * (40000 - 10000) + 0.20 * (80000 - 40000) + 0.25 * (income - 80000)
print("Tax owed: $", tax)

# Exercise 3-2
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, " is a leap year.")
else:
    print(year, " is not a leap year.")

# Exercise 3-3
weight = float(input("Enter your weight (in kilograms or grams): "))
height = float(input("Enter your height (in meters or centimeters): "))

if weight > 200:            # assuming nobody weighs more than 200kg
    weight = weight / 1000  # from grams to kilograms
if height > 3:              # assuming nobody is taller than 3 meters
    height = height / 100   # from centimeters to meters

BMI = weight / (height ** 2)
print("Your BMI is", BMI)
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI <= 24.9:
    print("You are of normal weight.")
elif 25 <= BMI <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")