# PALISSON Antoine

### Level - Easy
## Exercise 1-1
person = {"name": "John", "age": 30, "job": "Developer"}
print(person["name"])

## Exercise 1-2
prices = {"apple": 0.5, "banana": 0.25, "orange": 0.75}
prices["banana"] = 0.3
prices["cherry"] = 0.1
prices.update({"pear": 0.7})
print(prices)

## Exercise 1-3
car = {"brand": "Toyota", "model": "Camry", "color": "Red", "year": 2022}
print(car.keys())
print(car.values())

## Exercise 1-4
list_of_tuples = [('square', 'blue'), ('triangle', 'red'), ('circle', 'yellow')]
dict_from_list = dict(list_of_tuples)
dict_from_list["rectangle"] = "green"
del dict_from_list["circle"]
form = dict_from_list.pop("triangle")
print(list(dict_from_list.items()))

## Exercise 1-5
colors = {"red", "green", "blue"}
colors_alt1 = set(["red", "green", "blue"])
colors.remove("green")
colors.discard("yellow")
colors.update(["Purple", "Pink"])
print(len(colors))
colors.clear()
del colors

## Exercise 1-6
num_set = {5, 1, 3, 7, 8, 2, 3}
print(num_set)  
# Observation: The order is not preserved
print(max(num_set))
print(min(num_set))
num_set.update([False, 3.14, "Rose"])
print(num_set)  
# Observation: The order is based on the hash value of the elements, it's not ordered
num_set.add(1)  
# Observation: Adding 1 again will not change anything because sets only allow unique values

## Exercise 1-7
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print("apple" in fruits)

### Level - Moderate
## Exercise 2-1
inventory = {"apples": 10, "bananas": 12, "cherries": 34}
print("bananas" in inventory.keys())
print(5 in inventory.values())
fruits = {"apples", "bananas", "cherries"}
if len(inventory) > len(fruits):
    print("Inventory has more items than fruits set.")
else:
    print("Fruits set has more or equal items than inventory.")

## Exercise 2-2
employees = {}
employees["John"] = {"job_title": "Developer", "salary": 5000}
employees["Jane"] = {"job_title": "Manager", "salary": 6000}
print(employees["John"]["salary"])

## Exercise 2-3
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

if 5 in A:
    B.add(5)
else:
    B.discard(5)

if 2 not in B:
    A.discard(2)

print(A, B)

if A & B:
    print("Common elements:", A & B)
else:
    print("No common elements.")

## Exercise 2-4
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]
common_elements = set(list1) & set(list2) & set(list3)
print(common_elements)

## Exercise 2-5
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {4, 5}
D = {7, 8}

print("C is a subset of A:", C.issubset(A))
print("C is a subset of B:", C.issubset(B))
print("A is a superset of C:", A.issuperset(C))

if A & B:
    print("Common elements between A and B:", A & B)
else:
    print("A and B have no common elements.")

print("C and D are disjoint:", C.isdisjoint(D))

## Exercise 2-6
C = {1.1, 2.2, 3.3}
if sum(C) > 6:
    C.add("valid")
else:
    C.add("invalid")
D = C - {"valid", "invalid"}
print(D)

## Exercise 2-7
A = {1, 3, 5, 7}
B = {2, 3, 6, 8}
print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))

### Level - Hard
## Exercise 3-1
countries = {
    "China": {
        "Pekin": {"population": 21000000, "landmarks": ["The Summer Palace"]},
        "Xi'an": {"population": 4000000, "landmarks": ["Terracotta Warriors"]}
    },
    "France": {
        "Paris": {"population": 2000000, "landmarks": ["Eiffel Tower"]}
    }
}

country_name = "China"
city_name = "Pekin"
print("Population of", city_name + ",", country_name, ":", countries[country_name][city_name]['population'])