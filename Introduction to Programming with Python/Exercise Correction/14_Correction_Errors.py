# PALISSON Antoine

### Level Easy
## Exercise 1-1
print("\nExercise 1-1")

def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

divide_numbers()

## Exercise 1-2
print("\nExercise 1-2")

def get_integer_from_user():
    while True:
        try:
            value = int(input("Enter an integer: "))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

get_integer_from_user()

## Exercise 1-3
print("\nExercise 1-3")

def dictionary_lookup():
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    try:
        key = input("Enter a key: ")
        print("Value:", dictionary[key])
    except KeyError:
        print("Key not found in dictionary.")

dictionary_lookup()

## Exercise 1-4
print("\nExercise 1-4")

def list_index_lookup():
    my_list = [1, 2, 3, 4, 5]
    try:
        index = int(input("Enter an index: "))
        print("Element at index:", my_list[index])
    except IndexError:
        print("Index out of range.")
    except ValueError:
        print("Please enter a valid integer.")

list_index_lookup()

## Exercise 1-5
print("\nExercise 1-5")

def open_file():
    try:
        file_name = input("Enter the name of the file to open: ")
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

open_file()

## Exercise 1-6
print("\nExercise 1-6")

def check_age():
    try:
        age = int(input("Enter your age: "))
        assert age > 0, "Age must be a positive integer."
        print("Your age is:", age)
    except AssertionError as error:
        print("Assertion Error:", error)
    except ValueError:
        print("Please enter a valid integer for age.")

check_age()

### Level Moderate
## Exercise 2-1
print("\\nExercise 2-1")

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        else:
            raise ValueError("Invalid operation")
    except ValueError as ve:
        print("Error:", ve)
    else:
        print("Result:", result)
    finally:
        print("Calculation completed.")

calculator()

## Exercise 2-2
print("\nExercise 2-2")

def sum_numbers_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            numbers = [float(line.strip()) for line in file]
        return sum(numbers)
    except FileNotFoundError:
        print("File not found.")
        return None
    except ValueError:
        print("The file contains non-numeric values.")
        return None
    finally:
        if 'file' in locals():
            file.close()
            print("File closed.")

sum_ = sum_numbers_in_file('myfile.txt')
print("Sum:", sum_)

## Exercise 2-3
print("\nExercise 2-3")

def nested_try_except(file_name):
    try:
        try:
            with open(file_name, 'r') as file:
                number = float(file.read())
        except FileNotFoundError as fnf_error:
            print("File not found:", fnf_error)
            raise
        except ValueError as ve:
            print("Non-numeric value in the file:", ve)
            raise
        
        result = 100 / number
        print("Result:", result)

    except ZeroDivisionError as zde:
        print("Zero division error:", zde)

nested_try_except('myfile.txt')