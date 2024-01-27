# PALISSON Antoine

### Level Easy
from datetime import datetime
import os
from collections import Counter
import csv
import random

## Exercise 1-1
print("\nExercise 1-1")

def days_until_end_of_year():
    today = datetime.now()
    end_of_year = datetime(today.year, 12, 31)
    return (end_of_year - today).days

print(f"Days until end of year: {days_until_end_of_year()}")

## Exercise 1-2
print("\nExercise 1-2")

def list_files_in_directory():
    files_info = []
    for file in os.listdir():
        if os.path.isfile(file):
            size = os.path.getsize(file)
            files_info.append((file, size))
    return files_info

for file, size in list_files_in_directory():
    print(f"File: {file}, Size: {size} bytes")

## Exercise 1-3
print("\nExercise 1-3")

def count_characters(string):
    counter = Counter(string)
    return counter.most_common(3)

test_string = "example string for counting"
print(f"Most common characters in '{test_string}': {count_characters(test_string)}")

## Exercise 1-4
print("\nExercise 1-4")

def average_age_from_csv(file_path):
    total_age = 0
    count = 0
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[1].isdigit():
                total_age += int(row[1])
                count += 1
    return total_age / count
print(f"Average Age: {average_age_from_csv('mycsvfile.csv')}")

## Exercise 1-5
print("\nExercise 1-5")

def generate_random_numbers():
    return random.sample(range(1, 101), 5)

print(f"Random numbers: {generate_random_numbers()}")

### Level Moderate
from datetime import datetime, timedelta
import random
from collections import Counter
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Exercise 2-1
print("\nExercise 2-1")

def generate_random_dates():
    year = datetime.now().year
    dates = [datetime(year, 1, 1) + timedelta(days=random.randint(0, 364)) for _ in range(100)]
    return dates

def count_dates_by_month(dates):
    month_counter = Counter(date.month for date in dates)
    return month_counter

random_dates = generate_random_dates()
print("Dates count by month:", count_dates_by_month(random_dates))

## Exercise 2-2
print("\\nExercise 2-2")

def generate_random_integers(n):
    return [random.randint(1, 100) for _ in range(n)]

ml1 = generate_random_integers(50)
ml2 = generate_random_integers(50)

print("List 1 - Mean:", statistics.mean(ml1), 
      "Median:", statistics.median(ml1), 
      "Std Dev:", statistics.stdev(ml1))
print("List 2 - Mean:", statistics.mean(ml2), 
      "Median:", statistics.median(ml2), 
      "Std Dev:", statistics.stdev(ml2))

## Exercise 2-3
print("\nExercise 2-3")

def plot_sales_per_product(csv_file):
    df = pd.read_csv(csv_file)
    total_sales = df.groupby('Product')['Sales'].sum()
    total_sales.plot(kind='bar')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.title('Sales per Product')
    plt.show()

plot_sales_per_product("sales_data.csv")

## Exercise 2-4
print("\nExercise 2-4")

def matrix_operations():
    matrix = np.random.randint(1, 101, (5, 5))
    normalized_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())
    row_sums = normalized_matrix.sum(axis=1)
    column_sums = normalized_matrix.sum(axis=0)
    determinant = np.linalg.det(matrix)

    # Refer to the last part of the course to understand the try-except statement
    try:
        inverse_matrix = np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        inverse_matrix = None

    print("Matrix:", matrix)
    print("Normalized Matrix:", normalized_matrix)
    print("Row Sums:", row_sums)
    print("Column Sums:", column_sums)
    print("Determinant:", determinant)
    print("Inverse Matrix:", inverse_matrix if inverse_matrix is not None else "Not invertible")

matrix_operations()