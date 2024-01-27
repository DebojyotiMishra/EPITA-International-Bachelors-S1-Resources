# PALISSON Antoine

### Level - Easy
## Exercise 1-1
print("\nExercise 1-1")
list1 = [i for i in range(1,6)]
print(list1)

list2 = [i for i in range(0,9,2)]
print(list2)

## Exercise 1-2
print("\nExercise 1-2")
initial_list1 = [4,24,44,64,94]
added_6_list = [i+6 for i in initial_list1]
print(added_6_list)

initial_list2 = [2,4,6,8,10]
squared_list = [i**2 for i in initial_list2]
print(squared_list)

## Exercise 1-3
print("\nExercise 1-3")
string = "hello"
char_list = [c for c in string]
print(char_list)

## Exercise 1-4
print("\nExercise 1-4")
dict_squares = {i: i**2 for i in range(1,6)}
print(dict_squares)

## Exercise 1-5
print("\nExercise 1-5")
word_list = ["apple", "banana", "cherry"]
word_length_dict = {word: len(word) for word in word_list}
print(word_length_dict)

## Exercise 1-6
print("\nExercise 1-6")
int_list = [1,2,3,4,5,6,7,8,9]
odd_set = {i for i in int_list if i % 2 != 0}
print(odd_set)

### Level - Moderate
## Exercise 2-1
print("\nExercise 2-1")
tuple_list = [("a", 5), ("b", 15), ("c", 11), ("d", 7)]
dict_from_tuples = {k: v for k, v in tuple_list if v > 10}
print(dict_from_tuples)

## Exercise 2-2
print("\nExercise 2-2")
given_string = "comprehension"
char_count_dict = {char: given_string.count(char) for char in set(given_string)}
print(char_count_dict)

## Exercise 2-3
print("\nExercise 2-3")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
symmetric_diff = {x for x in set1.union(set2) if x not in set1.intersection(set2)}
print(symmetric_diff)

## Exercise 2-4
print("\nExercise 2-4")
given_dict = {"a": "one", "b": "two", "c": "three", "d": "four"}
inverted_dict = {v: k for k, v in given_dict.items()}
print(inverted_dict)

## Exercise 2-5
print("\nExercise 2-5")
word_list = ["cat", "elephant", "dog", "ant"]
word_length_classification = {word: "short" if len(word) <= 3 else "long" for word in word_list}
print(word_length_classification)

### Level - Hard
## Exercise 3-1
print("\nExercise 3-1")
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)

## Exercise 3-2
print("\nExercise 3-2")
words = ["apple", "banana", "cherry", "date", "kiwi"]
filtered_words = [word for word in words if len(word) > 3 and 'e' in word]
print(filtered_words)

## Exercise 3-3
print("\nExercise 3-3")
set1 = {10, 15, 20, 25, 30}
set2 = {5, 15, 25, 35, 45}
common_multiples = {x for x in set1.intersection(set2) if x % 3 == 0 and x % 5 == 0}
print(common_multiples)

## Exercise 3-4
print("\nExercise 3-4")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transposed_matrix)

## Exercise 3-5
print("\nExercise 3-5")
divisors = range(2, 10)
numbers = [num for num in range(1, 101) if any(num % divisor == 0 for divisor in divisors)]
print(numbers)

### Level - very Hard
print("\nExercise Very Hard")
fizzbuzz = [print("Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0)) 
            if i % 3 == 0 or i % 5 == 0 
            else print(i) 
            for i in range(1, 101)]