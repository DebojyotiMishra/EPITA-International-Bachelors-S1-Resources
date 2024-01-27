# PALISSON Antoine

## Exercise 1
print("\nExercise 1")

def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)
    
print(sum_of_natural_numbers(5))

## Exercise 2
print("\nExercise 2")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))

## Exercise 3
print("\nExercise 3")

def reverse_string(s):
    if len(s) == 0 or len(s) == 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
print(reverse_string("Hello World!"))

## Exercise 4
print("\nExercise 4")
def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n-1)

def find_min(arr):
    if len(arr) == 1:
        return arr[0]
    prev_min = find_min(arr[1:])
    if arr[0] < prev_min:
        return arr[0]
    else:
        return prev_min

def is_sorted(arr):
    if len(arr) == 1:
        return True
    return arr[0] <= arr[1] and is_sorted(arr[1:])

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

## Exercise 5
print("\nExercise 5")

def list_sum(lst):
    sum_ = 0
    for element in lst :
        if isinstance(element, list) :
            sum_ += list_sum(element)
        else :
            sum_ += element
    return sum_
   
print(list_sum([1,2, [3,4,[5,6]]]))

## Exercise 6
print("\nExercise 6")

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(f"The GCD of 36 and 52 is: {gcd(36, 52)}")

## Exercise 7
print("\nExercise 7")

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        disk = source[1].pop()
        target[1].append(disk)
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    disk = source[1].pop()
    target[1].append(disk)
    tower_of_hanoi(n-1, auxiliary, source, target)

tower = [5,4,3,2,1]
tower_of_hanoi(len(tower), ("A", tower), ("B",[]), ("C", []))