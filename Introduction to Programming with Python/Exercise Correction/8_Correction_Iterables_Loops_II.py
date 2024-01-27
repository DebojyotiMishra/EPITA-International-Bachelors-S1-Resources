# PALISSON Antoine

### Level - Easy
## Exercise 1-1
print("\nExercise 1-1")

n = int(input("Enter a number: "))
count = 1
while count <= n:
    print(count)
    count += 1

## Exercise 1-2
print("\nExercise 1-2")

n = int(input("Enter a number: "))
while n >= 1:
    print(n)
    n -= 1

## Exercise 1-3
print("\nExercise 1-3")

n = int(input("Enter a number: "))
count = 1
total = 0
while count <= n:
    total += count
    count += 1
print("Total:", total)

## Exercise 1-4
print("\nExercise 1-4")

n = int(input("Enter a number: "))
count = 2
total = 0
while count <= n:
    total += count
    count += 2
print("Total:", total)

## Exercise 1-5
print("\nExercise 1-6")

n = int(input("Enter a starting number: "))
while n <= 1000:
    n *= 2
    print(n)

### Level - Moderate
## Exercise 2-1
print("\nExercise 2-1")

n = int(input("Enter a number: "))
count = 1
while count <= n:
    if count % 5 == 0:
        print(count)
    count += 1

## Exercise 2-2
print("\nExercise 2-2")

number = 8
guess = int(input("Guess a number between 1 and 10: "))
tries = 1
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1
print(f"Correct! It took you {tries} tries.")

## Exercise 2-3
print("\nExercise 2-3")

number = 6
attempts = 0
while attempts < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed correctly!")
        break
    attempts += 1
if attempts == 3:
    print("Sorry, you've run out of attempts. Better luck next time!")

## Exercise 2-4
print("\nExercise 2-4")

continue_calculator = "yes"
while continue_calculator.lower() == "yes":
    operation = input("Enter the operation in format 'x operator y': ")
    result = eval(operation)
    print(f"The result is: {result}")
    continue_calculator = input("Do you want to continue? (yes/no): ")

## Exercise 2-5
print("\nExercise 2-5")

n = int(input("Enter a number to generate its Collatz sequence: "))
print(n, end=" -> ")
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n, end=" -> ")
print("End")

## Exercise 2-6
print("\nExercise 2-6")

number = 75
low_boundary = 1
high_boundary = 100
guess = None
while guess != number:
    guess = int(input(f"Guess a number between {low_boundary} and {high_boundary}: "))
    if guess == number:
        print("Congratulations! You guessed the correct number!")
    elif guess < number:
        low_boundary = guess + 1
        print("Your guess is too low.")
    else:
        high_boundary = guess - 1
        print("Your guess is too high.")

## Exercise 2-7
print("\nExercise 2-7")

integer_list = [4,8,25,4,69,2,78,-5,0,3,6]
index = 0
total = 0
while index < len(integer_list) and integer_list[index] >= 0:
    total += integer_list[index]
    index += 1
print(f"The sum is: {total}") 

### Level - Hard
## Exercise 3-1
print("\nExercise 3-1")

message = input("Enter a message (lowercase letters only): ")
encrypted_message = ""
alphabet = ' abcdefghijklmnopqrstuvwxyz'
index = 0
while index < len(message):
    new_index = (alphabet.index(message[index]) + 1 * index) % 27
    encrypted_message += alphabet[new_index]
    index += 1
print(f"Encrypted message: {encrypted_message}")

decrypted_message = ""
index = 0
while index < len(encrypted_message):
    new_index = (alphabet.index(encrypted_message[index]) - 1 * index) % 27
    decrypted_message += alphabet[new_index]
    index += 1
print(f"Decrypted message: {decrypted_message}")

## Exercise 3-2
print("\nExercise 3-2")

n = float(input("Enter a positive number: "))
x0 = n / 2
tolerance = 0.0001
steps = 0
while True:
    x1 = (x0 + n / x0) / 2
    if abs(x1 - x0) < tolerance:
        break
    x0 = x1
    steps += 1
print(f"Approximated square root: {x1}")
print(f"Steps to reach approximation: {steps}")

## Exercise 3-3
print("\nExercise 3-3")

n = int(input("Enter a number: "))
smallest_multiple = n
steps = 0

while True:
    steps += 1

    all_true = True
    for i in range(1, n + 1):
        if smallest_multiple % i != 0 :
            all_true = False
            break
        
    if all_true:
        break
    # here, we increment by n because the smallest multiple has to be a multiple of n
    smallest_multiple += n  
    

print(f"The smallest number divisible by every number from 1 to {n} is: {smallest_multiple}")
print(f"Number of steps: {steps}")