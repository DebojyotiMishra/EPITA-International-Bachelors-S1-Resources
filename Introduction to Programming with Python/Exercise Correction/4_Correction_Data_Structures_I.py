# PALISSON Antoine

### Level - Easy
## Exercise 1-1
fruits = ["apple", "banana", "cherry"]
print(fruits)

vegetables = ("carrot", "broccoli", "lettuce")
print(vegetables)

## Exercise 1-2
colors = ["red", "blue", "green", "yellow", "pink"]
print(colors[1], colors[3])

grades = ("A", "B", "C", "D", "F")
print(grades[0], grades[-1])

## Exercise 1-3
days = ["Monday", "Tuesday", "Wendesday", "Thursday", "Friday"]
days[2] = "Wednesday"
print(days)

## Exercise 1-4
animals = ["cat", "dog", "apple"]
animals.remove("apple")
print(animals)

animals.append("rabbit")
print(animals)

## Exercise 1-5
months = ("Jan", "Feb", "Mach", "Apr")
# Observation: You can't modify a tuple, so this will cause an error:
# months[2] = "March" 

month_list = list(months)
month_list[2] = "March"
months = tuple(month_list)
print(months)

## Exercise 1-6
fishes = ["catfish", "perch", "cod", "carp"]
print(fishes[-1])
print(fishes[3])

fishes[1] = "salmon"
print(fishes)

## Exercise 1-7
numbers = (0, 0, 1, 0, 1, 1)
print(numbers.count(0))
print(numbers.index(1))

del numbers
# Observation: You can't print "numbers" after this line, as it no longer exists.

## Exercise 1-8
first_list = [0, 1, 2, 3, 4]
copy_list = first_list
copy_list[-1] = 99
print(first_list) 
# Observation: The first list has been changed ! It will print [0, 1, 2, 3, 99]
copy_list = first_list.copy() 
# OR copy_list = list(first_list)
# OR copy_list = first_list[:]

first_list = [0, 1, 2, 3, 4]
copy_list[-1] = 44
print(first_list)

### Level - Moderate
# Exercise 2-1
integers = [0, 1, 3]
integers.append(4)
# OR integers += [4]
integers.insert(2, 2)
print(integers)
new_list = [5, 6, 7, 8]
integers.extend(new_list)
integers.remove(0)
print(integers)

## Exercise 2-2
floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8]
print(floats[1:4])
print(floats[2:])
print(floats[:5])
print(floats[::-1])

## Exercise 2-3
mylist = ['abc', False, 1, 3.14159]
mylist[1:3] = [True, 0]
var_abc = mylist.pop(0)
print(var_abc)
var1, var2, var3 = mylist
print(var1, var2, var3)

## Exercise 2-4
numbers = [3, 4, 5, 1, 2]
user_number = float(input("Enter a number: "))
if user_number > max(numbers):
    print("The number you entered is higher than the maximum of the list.")
else:
    print("The number you entered is lower than the maximum of the list.")

## Exercise 2-5
sports = ["Football", "Basketball", "Swimming", "Tennis"]
favorite_sport = input("What's your favorite sport? ")
if favorite_sport in sports:
    print("We love that too!")


### Level - Hard
## Exercise 3-1
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
tup = (num1, num2, num3)
if tup[0] + tup[1] > tup[2]:
    print(tup[::-1])
else:
    print(tup)

## Exercise 3-2
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(values[-2::-2])

## Exercise 3-3
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[2][1])
print(matrix[1])
print([matrix[0][-1]] + [matrix[1][-1]] + [matrix[2][-1]])
print([matrix[0][0]] + [matrix[1][1]] + [matrix[2][2]])

## Exercise 3-4
list1 = [0, 1]
list2 = ['on', 'off']
list3 = [True, False]

resulting_tuple = (list1 + [tuple(list1[::-1])], 
                   tuple(list2), 
                   [list2[::-1] + list3, 
                   list3])
print(resulting_tuple)