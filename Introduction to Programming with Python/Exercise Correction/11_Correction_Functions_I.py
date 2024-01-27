# PALISSON Antoine

### Level - Easy
## Exercise 1-1
print("\nExercise 1-1")

def greet(name):
    return f"Hello, {name}!"
result = greet("Alice")
print(result)

## Exercise 1-2
print("\nExercise 1-2")

def remainder(num1, num2):
    return num1 % num2
result = remainder(10, 3)
print(result)

## Exercise 1-3
print("\nExercise 1-3")

def rectangle_area(width, height):
    return width * height
result = rectangle_area(5, 4)
print(result)

## Exercise 1-4
print("\nExercise 1-4")

def power(number, exponent=2):
    return number ** exponent
result = power(3)
print(result)
result = power(3, 3)
print(result)

## Exercise 1-5
print("\nExercise 1-5")

def reverse_string(s):
    return s[::-1]
result = reverse_string("Hello")
print(result)

### Level - Moderate
## Exercise 2-1
print("\nExercise 2-1")

def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
result = average([1, 2, 3, 4, 5])
print(result)

## Exercise 2-2
print("\nExercise 2-2")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
result = factorial(5)
print(result)

## Exercise 2-3
print("\nExercise 2-3")

def max_in_list(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value
result = max_in_list([3, 1, 4, 1, 5, 9, 2, 6])
print(result)


## Exercise 2-4
print("\nExercise 2-4")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
result = is_prime(7)
print(result)

## Exercise 2-5
print("\nExercise 2-5")

def safe_divide(a, b):
    return a / b if b != 0 else None
def compute_details(a, b):
    sum_ = a + b
    difference = a - b
    product = a * b
    quotient = safe_divide(a, b)
    return sum_, difference, product, quotient
result = compute_details(10, 2)
print(result)

## Exercise 2-6
print("\nExercise 2-6")

def is_perfect(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n
result = is_perfect(28)
print(result)

## Exercise 2-7
print("\nExercise 2-7")
def calculate(a, b=None, c=None):
    if a and not b and not c:
        return a**2
    elif a and b and not c:
        return a + b
    else:
        return (a + b)/2
print(calculate(5))        
print(calculate(5, 3))     
print(calculate(5, 3, 2)) 
