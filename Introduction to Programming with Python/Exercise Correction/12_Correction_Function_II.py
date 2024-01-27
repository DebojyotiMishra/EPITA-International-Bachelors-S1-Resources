# PALISSON Antoine

## Level Easy
# Exercise 1-1
print("\nExercise 1-1")
def sum_all(*args):
    if args:
        return sum(args)
    else :
        return "No arguments provided"

print(sum_all(1, 2, 3))
print(sum_all(10, 20))
print(sum_all())

# Exercise 1-2
print("\nExercise 1-2")
def count_args(*args):
    if args:
        return len(args)  
    else :
        return "No arguments provided"

print(count_args(1, 2, 3))
print(count_args("a", 2, 3.14, True))
print(count_args())

# Exercise 1-3
print("\nExercise 1-3")
def concat_strings(*args):
    if args:
        return ' '.join(args)  
    else :
        return "No arguments provided"

print(concat_strings("Hello", "World!")) 
print(concat_strings("Is", "Python", "fun", "?"))

# Exercise 1-4
print("\nExercise 1-4")
def filter_by_type(**kwargs):
    types_dict = {}
    for _, value in kwargs.items():
        if type(value) in types_dict:
            types_dict[type(value)].append(value)
        else:
            types_dict[type(value)] = [value]
    return types_dict

print(filter_by_type(name="Alice", age=30, city="New York", score=85.5))

# Exercise 1-5
print("\nExercise 1-5")
def update_dict(original, **kwargs):
    original.update(kwargs)
    return original

dictio = {'a': 1, 'b': 2}
print(update_dict(dictio, b=3, c=4))

# Exercise 1-6
print("\nExercise 1-6")
sum_lambda = lambda x, y: x + y

print(sum_lambda(5, 3))

## Level Moderate
# Exercise 2-1
print("\nExercise 2-1")
def multiply_and_sum(multiplier=1, *args):
    if args:
        return sum(x * multiplier for x in args)
    else :
        return "No arguments provided"

print(multiply_and_sum(2, 1, 2, 3))
print(multiply_and_sum(3, 4, 5))
print(multiply_and_sum())

# Exercise 2-2
print("\nExercise 2-2")
sort_by_second = lambda items: sorted(items, key=lambda x: x[1])

print(sort_by_second([(5, 3), (2, 2), (4, 7), (0, 1), (1, 6)]))

# Exercise 2-3
print("\nExercise 2-3")
filter_even = lambda numbers: list(filter(lambda x: x % 2 == 0, numbers))

print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Exercise 2-4
print("\nExercise 2-4")
find_intersection = lambda list1, list2: list(filter(lambda x: x in list2, list1))

print(find_intersection([0, 3, 5, 6, 7, 8, 10], [1, 3, 4, 5, 7, 8]))

# Exercise 2-5
print("\nExercise 2-5")
square_elements = lambda numbers: list(map(lambda x: x ** 2, numbers))

print(square_elements([1, 2, 3, 4, 5]))

# Exercise 2-6
print("\nExercise 2-6")
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(list(map(lambda x, y: x + y, l1, l2)))

# Exercise 2-7
print("\nExercise 2-7")
def greet(name):
    def message():
        return f"Hello, {name}!"
    return message()

print(greet("Alice"))

# Exercise 2-8
print("\nExercise 2-8")
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print(double(5))
print(triple(3))

# Exercise 2-9
print("\nExercise 2-9")
def create_counter():
    count = []
    def counter():
        count.append(1)
        return len(count)
    return counter

counter = create_counter()
print(counter())
print(counter())
print(counter())

## Level Hard
print("\nExercise 3-1")
# Exercise 3-1
sort_by_model = lambda items: sorted(items, key=lambda x: x['model'])
sort_by_model_color = lambda items: sorted(items, key=lambda x: (x['model'], x['color']))

cars = [{'model': 7, 'color': 'Black'}, {'model': 2, 'color': 'White'}, 
        {'model': 7, 'color': 'Blue'}, {'model': 2, 'color': 'Gold'},
        {'model': 3, 'color': 'Yellow'}, {'model': 3, 'color': 'Pink'}]

print(sort_by_model(cars))
print(sort_by_model_color(cars))

# Exercise 3-2
print("\nExercise 3-2")
l1 = [-1, 2, -3, 5, 1, 0, 7, 8, 9, -10]
sort_negative = lambda x:-1/(1e-10 + x) # 1e10 is there to avoid division by 0
print(sorted(l1, key=sort_negative))

# Exercise 3-3
print("\nExercise 3-3")
import random

def password_generator(char_sets="123456789"):
    def generate_password(length):
        characters = ''.join(char_sets)
        password = []
        for _ in range(length):
            password += random.choice(characters)
        return ''.join(password)
    return generate_password

alpha_generator = password_generator(['abcdefg', 'hijklmnop'])
numeric_generator = password_generator(['123456789'])
print(alpha_generator(10))
print(numeric_generator(6))