# PALISSON Antoine

### Level - Easy
## Exercise 1-1

name = "Your Name"
age = 25
country = "Your Country"
print(age)
print(country)

## Exercise 1-2

print(type(5))
print(type(5.0))
print(type("5"))
print(type(True))
# Observation: Note the differences in types even if the values appear similar.

## Exercise 1-3

x = 10 
print(x)
print(type(x))
x = "Hello" 
print(x)
# Observation: Note how the type of variable x changes based on its content.

## Exercise 1-4

int_value = int("123")
print(int_value)

# Convert integer to string
str_value = str(123)
print(str_value)

# Convert string to float
float_value = float("123.45")
print(float_value)

## Exercise 1-5

a = 5
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)   # Division, result is a float
print(a // b)  # Floor division, result is an integer
print(a % b)   

## Exercise 1-6

radius = 5
pi = 3.14
area = pi * radius ** 2
print(area)

### Level - Moderate
## Exercise 2-1

x, y, z = 7, 4, 1
x = x + 5
y = y - 10
z = z * 2
print(x, y, z)

## Exercise 2-2

firstName = "YourFirstName"
lastName = "YourLastName"
fullName = firstName + " " + lastName
print("My name is", fullName)

## Exercise 2-3

firstName = input("Please enter your first name: ")
print(type(firstName))
lastName = input("Please enter your last name: ")
print("My name is", firstName, lastName)

## Exercise 2-4

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
print(type(num1))
print(type(num2))
num1 = int(num1)
num2 = int(num2)
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
division_result = num1 / num2
print("Division:", division_result)
print(type(division_result))

## Exercise 2-5

value = 10
value = value * 5
value = str(value) + " is a big number"
print(value)

### Level - Hard
# Exercise 3-1

age = int(input("Enter your current age: "))
years = int(input("How many years into the future do you want to look? "))
newAge = age + years
print("In", years, "years, you will be", newAge, "years old.")

# Exercise 3-2: Swapping values of two variables

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Swapping method 1: With a temporary variable
temp = a
a = b
b = temp
print("After first swapping: a =", a, "b =", b)

# Swapping method 2: Without using a temporary variable
a, b = b, a
print("After second swapping: a =", a, "b =", b)