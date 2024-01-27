# PALISSON Antoine

### Level - Easy
## Exercise 1-1
print("\nExercise 1-1:")

colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)

## Exercise 1-2
print("\nExercise 1-2:")

sum_of_numbers = 0
for i in range(10):
    print(i)
    sum_of_numbers += i
print("Sum:", sum_of_numbers)

## Exercise 1-3
print("\nExercise 1-3:")

sentence = "Hello, world!"
count = 0
for char in sentence:
    if char == 'l':
        count += 1
print(f"The letter 'l' appears {count} times in the sentence.")

## Exercise 1-4
print("\nExercise 1-4:")

for i in range(2, 21, 2):
    print(i)

## Exercise 1-5
print("\nExercise 1-5:")

fruits = ["apple", "banana", "cherry"]
duplicated_fruits = []
for fruit in fruits:
    duplicated_fruits.append(fruit)
    duplicated_fruits.append(fruit)
print(duplicated_fruits)

## Exercise 1-6
print("\nExercise 1-6:")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

## Exercise 1-7
print("\nExercise 1-7:")

for i in range(-10, 1):
    print(i)
for i in range(0, -11, -2): 
    print(i)

### Level - Moderate
## Exercise 2-1
print("\nExercise 2-1:")

word = "algorithm"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for char in word:
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")

## Exercise 2-2
print("\nExercise 2-2:")

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []
for elem in list1:
    if elem in list2:
        common_elements.append(elem)
print(f"Common elements: {common_elements}")

## Exercise 2-3
print("\nExercise 2-3:")

user_string = input("Enter a string: ")
is_palindrome = True
for i in range(len(user_string) // 2): 
    if user_string[i] != user_string[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

## Exercise 2-4
print("\nExercise 2-4:")

n = int(input("Enter a number: "))
factorials = [1]
for i in range(1, n+1):
    factorials.append(factorials[-1] * i)
print(factorials[1:])

## Exercise 2-5
print("\nExercise 2-5:")

matrix = []
num = 1
for i in range(3):
    row = []
    for j in range(3):
        row.append(num)
        num += 1
    matrix.append(row)
print(matrix)

## Exercise 2-6
print("\nExercise 2-6:")

students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "History", "Biology"]
for student, subject in zip(students, subjects):
    print(f"{student} needs to study {subject}.")

## Exercise 2-7
print("\nExercise 2-7:")

user_number = int(input("Enter an integer: "))
for i in range(user_number + 1, user_number + 11):
    print(i)

## Exercise 2-8
print("\n\nExercise 2-8:")

integers = [1, 2, 3, 4, 5, 6]
new_list = []
for i in range(len(integers)):
    new_list.append(integers[0])
    del integers[0]
print(f"Original list (now empty): {integers}")
print(f"New list: {new_list}")

## Exercise 2-9
print("\nExercise 2-9:")

lst = ["a", "b", "c", "d"]
for index, value in enumerate(lst):
    print(f"{index} : {value}")

## Exercise 2-10
print("\nExercise 2-10:")

data = [3, 5, 7, 3, 5, 9, 1, 7]
unique_data = []
for num in data:
    if data.count(num) == 1:
        unique_data.append(num)
print(unique_data)

### Level - Hard
## Exercise 3-1
print("\nExercise 3-1:")

a, b = 0, 1
fib_sequence = []
for _ in range(10):
    fib_sequence.append(a)
    a, b = b, a+b
print(fib_sequence)

## Exercise 3-2
print("\nExercise 3-2:")

for num in range(20, 61):
    is_prime = True
    for i in range(2, num//2):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

## Exercise 3-3
print("\nExercise 3-3:")

nums = [2, 5, 3, 5, 8, 9, 5, 2, 3]
cpt = {}
for num in nums:
    if cpt.get(num) :
        cpt[num] += 1
    else :
        cpt[num] = 1

max_ = 0
for k,v in cpt.items():
    if v > max_ : 
        mode, max_ = k, v
print(f"The mode is: {mode}")

## Exercise 3-4
print("\nExercise 3-4:")

n = 3
for i in range(0,n):
    spaces = " " * ((2*n-2*i-1)//2)
    stars = "*" * (2*i+1)
    print(spaces + stars + spaces)

# Exercise 3-5
print("\nExercise 3-6:")

s = "abc"
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i != j and j != k and i != k:
                print(s[i] + s[j] + s[k])

## Exercise 3-6
print("\nExercise 3-7:")

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print()
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

### Level - Very Hard
## Exercise 4-1
print("\nExercise 4-1:")

number = int(input("Enter a number (1-3999): "))

if 0 < number < 4000:
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    for i in range(len(val)):
        count = number // val[i]
        number %= val[i]
        for _ in range(count):
            roman_num += syms[i]
    print(roman_num)
else:
    print("Number out of range!")

## Exercise 4-2
print("\nExercise 4-2:")

n = 5
for i in range(1, n+1):
    for j in range(i):
        print('*', end=" ")
    print()
for i in range(n-1, 0, -1):
    for j in range(i):
        print('*', end=" ")
    print()