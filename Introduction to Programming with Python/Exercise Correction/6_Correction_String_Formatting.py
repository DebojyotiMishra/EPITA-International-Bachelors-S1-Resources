# PALISSON Antoine

### Level Easy
## Exercise 1-1
print("\nExercise 1-1:")

hello_world = "Hello, World!"
print(hello_world)
print(hello_world.upper())
print(hello_world.lower())
print(hello_world[0])
print(hello_world[-1])

## Exercise 1-2
print("\nExercise 1-2:")

sentence = "Learning Python is exciting."
print(sentence[9:15])
print(sentence[-9:-1])

## Exercise 1-3
print("\nExercise 1-3:")

name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

## Exercise 1-4
print("\nExercise 1-4:")

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
print(f"Hello {first_name} {last_name}! Welcome aboard!")

## Exercise 1-5
print("\nExercise 1-5:")

fruits_string = "Apples,Bananas,Cherries,Dates"
fruits_list = fruits_string.split(",")
fruits_joined = "-".join(fruits_list)
print(fruits_joined)

### Level - Moderate
## Exercise 2-1
print("\nExercise 2-1:")

var_string = "gibberishabc"
var_string = f"{var_string:.9}"
print(var_string)

## Exercise 2-2
print("\nExercise 2-2:")

university_string = "UnIvErSiTy"
print(university_string.capitalize())
if university_string.lower().endswith("ity"):
    print("The string ends with 'ity'.")
else:
    print("The string doesn't end with 'ity'.")

## Exercise 2-3
print("\nExercise 2-3:")

cat_string = "I like cats. Cats are cute."
dog_string = cat_string.replace("cats", "dogs").replace("Cats", "Dogs")
print(dog_string)

## Exercise 2-4
print("\nExercise 2-4:")

email = input("Enter your email address: ")
if "@" in email and email.endswith(".com"):
    print("Valid email.")
else:
    print("Invalid email.")

## Exercise 2-5
print("\nExercise 2-5:")

poem = """
Roses are red,
Violets are blue,
Sugar is sweet,
And so are you.
"""
print(f"Number of words in the poem: {len(poem.split())}")
poem = poem.replace("blue", "green").replace("you", "me")
print(poem)

## Exercise 2-6
print("\nExercise 2-6:")

string = "interior"
print(string[2:5]+string[4]+string[-2:])
rev_string = "abcdef"[::-1]
print(rev_string)

## Exercise 2-7
print("\nExercise 2-7:")

floats = [12.34567, 89.12345, 67.89123]
print(f"{floats[0]:10.2f}")
print(f"{floats[1]:10.2f}")
print(f"{floats[2]:10.2f}")

## Exercise 2-8
print("\nExercise 2-8:")

title_string = "Title Of The Book"
url_slug = title_string.lower().replace(" ", "-")
print(url_slug)

### Level - Hard
## Exercise 3-1
print("\nExercise 3-1:")

numbers = [1, 10, 100, 1000, 10000]
print(f"+{numbers[0]:>5}")
print(f"+{numbers[1]:>5}")
print(f"+{numbers[2]:>5}")
print(f"+{numbers[3]:>5}")
print(f"+{numbers[4]:>5}")

print(f"+{numbers[0]:0>5}")
print(f"+{numbers[1]:0>5}")
print(f"+{numbers[2]:0>5}")
print(f"+{numbers[3]:0>5}")
print(f"+{numbers[4]:0>5}")

## Exercise 3-2
print("\nExercise 3-2:")

sentence = "I am studying at the University in the year 2023"
transformed = "You " + sentence[2:16] + "a College" + sentence[32:-4] + "1999"
print(transformed)

## Exercise 3-3
print("\nExercise 3-3:")

string = "A:B:C:D:E:F"
parts = string.split(":")
result = ":".join(parts[-3:] + parts[:-3])
print(result)

## Exercise 3-4
print("\nExercise 3-4:")

sentence = "The quick brown fox"
words = sentence.split()
reversed_order = " ".join(words[::-1])
print(reversed_order)

## Exercise 3-5
print("\nExercise 3-5:")

word = "racecar"
pool = "cartracerace"

print(set(word)) # Which letters are in racecar ?

C1 = word.count('r') <= pool.count('r')
C2 = word.count('a') <= pool.count('a')
C3 = word.count('c') <= pool.count('c')
C4 = word.count('e') <= pool.count('e')

if C1 and C2 and C3 and C4 :
    print("Yes, 'racecar' can be constructed from 'cartracerace'.")
else :
    print("No, 'racecar' cannot be constructed from 'cartracerace'.")

## Exercise 3-6
word = input("Enter a word: ")
if not word.isalpha() :
    print("Your string is not a correct word.")
else:
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u'] :
        print(word + "way")
    else:
        print(word[1:] + word[0] + "ay")