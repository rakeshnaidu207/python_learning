"""Temperature Converter & Weather Advice
C or F) and the numerical degree.
Level 1 — Beginner
Write a program that converts temperatures between Celsius and Fahrenheit based on user input. Prompt for
the scale (
Formula: F = (C × 9/5) + 32 | C = (F - 32) × 5/9
If converted Celsius value is < 10, print "Cold"; if between 10 and 28, print "Mild"; if > 28, print "Hot"."""

""""user = input("Enter C or F: ")
temperature = float(input("Enter the temperature: "))

if user.lower() == "c":
    C = temperature
    F = (C * 9/5) + 32

    print("Fahrenheit:", round(F, 2))

    if C < 10:
        print("Cold")
    elif C >= 10 and C <= 28:
        print("Mild")
    else:
        print("Hot")

elif user.lower() == "f":
    F = temperature
    C = (F - 32) * 5/9

    print("Celsius:", round(C, 2))

    if C < 10:
        print("Cold")
    elif C >= 10 and C <= 28:
        print("Mild")
    else:
        print("Hot")

else:
    print("Please enter either C or F")"""

"""Number Classifier & Stat Collector
Write a function 
analyze_numbers(numbers) that accepts a list of integers and returns a dictionary containing
summary facts without using built-in functions (
sum , 
min , 
max , 
Keys required: 
total_count , 
sum_values , 
len ):
even_count , 
odd_count , 
min_val ,"""

"""def analyze_numbers(numbers):
    dictionary = {}
    sum=0
    for i in numbers:
        numbers.sort()
        sum+=i
        x=numbers[::2]
        y=numbers[::3]
        dictionary["total_count"]=len(numbers)
        dictionary["sum_values"]=sum
        dictionary["min_val"]=numbers[0]
        dictionary["max_val"]=numbers[-1]
        dictionary["even_count"]=x
        dictionary["odd_count"]=y
    return dictionary
print(analyze_numbers([1,2,5,6]))"""

"""print_diamond(n) that takes an odd integer n and prints a symmetric diamond of asterisks
(*). If an even integer is provided, raise a 
ValueError with a custom message"""

"""def print_diamond(n):
    if n %2 !=0:
            # Upper half including the middle row
            for i in range(n):
                spaces = " " * (n - i - 1)
                stars = "*" * (2 * i + 1)
                print(spaces + stars)

            # Lower half
            for i in range(n - 2, -1, -1):
                spaces = " " * (n - i - 1)
                stars = "*" * (2 * i + 1)
                print(spaces + stars)
    else:
        raise ValueError("Please provide an odd integer")
print_diamond(5)"""

"""Implement 
start and 
find_primes_in_range(start, end) using nested loops. Return a list of all prime numbers
between 
end (inclusive). Optimize by checking divisibility only up to √n."""

"""def find_primes_in_range(numbers):
    primes = []

    for number in numbers:
        if number < 2:
            continue

        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    return primes


print(find_primes_in_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))"""

"""Generate the first N terms of the Fibonacci sequence using an iterative approach, storing the results in a list.
Ensure your function handles inputs of N = 0 and N = 1 gracefully."""

"""n= int(input("Enter N: "))
h=[]
a=0
b=1
for  i in range(0,n):
     h.append(a)
     a,b=b,a+b
print(h)"""

""" Text Cleaning & Word Frequency
Write a function 
clean_and_count(text) that takes a string paragraph, removes punctuation characters,
converts text to lowercase, and returns a dictionary with word frequencies sorted by count descending."""

"""import string

def clean_and_count(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = text.lower().translate(str.maketrans('', '', string.punctuation))

    # Count word frequencies
    words = cleaned_text.split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) +1
    return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

text = "Hello, world! Hello Python. Python is great, and Python is easy."
print(clean_and_count(text))"""

"""List Flattening & De-duplication
Write a function 
flatten_and_unique(nested_list) that takes a multi-level nested list (e.g., 
[1, [2, 3,[4, 1]], 5] ) and flattens it into a 1D list with unique elements preserved in order of appearance."""
"""def flatten_and_unique(nested_list):
  g=[]
  for i in nested_list:
     for j in i:
          g.append(j)
  return g
print(flatten_and_unique([[1,2,3],[4,5,6],[7,8,9]]))"""


"""Dictionary Merging & Aggregation
Given a list of store sales dictionaries, e.g.,
[{"apple": 10, "banana": 5}, {"apple": 15, "orange":
8}] , write a function that aggregates total sales per item across all stores into a single summary dictionary."""

"""from collections import Counter
store_sales = [{"apple": 10, "banana": 5}, {"apple": 15, "orange": 8}]
summary_dict = {}
#Initialize an empty Counter before the loop
total_sales = Counter()
#Add each dictionary's counts to the running total
for store in store_sales:
    total_sales.update(store)
#Save the final combined data (converting Counter back to a regular dict)
summary_dict["total_sales"] = dict(total_sales)
print(summary_dict)"""

"""Given a list of integers and a target number, write a function 
two_sum(nums, target) that returns the indices
of the two numbers that add up to target. Optimize the lookup time to O(n) using a dictionary."""

"""def two_sum(nums, target):
    lookup = {}
    for i in range(len(nums)-1):
       if nums[i]+nums[i+1]==target:
           lookup["first_number"]=nums.index(nums[i])
           lookup["second_number"] = nums.index(nums[i+1])
    return lookup
print(two_sum([1,2,3,4,5,6,7,8,9,10],9))"""

"""Flexible Argument Aggregator
Create a function 
map ,
calculate_stats(*args, **kwargs) that accepts arbitrary numerical arguments alongside
operational keyword flags like 
scale=10 or 
operation="mean" to dynamically output calculated metrics."""

"""def calculate_stats(*args, **kwargs):
    operation = kwargs.get("operation", "sum")
    scale = kwargs.get("scale", 1)

    if operation == "sum":
        result = sum(args)

    elif operation == "mean":
        result = sum(args) / len(args)

    elif operation == "max":
        result = max(args)

    elif operation == "min":
        result = min(args)

    else:
        print("Invalid operation")
        return

    print("Result:", result * scale)
calculate_stats(10, 20, 40, operation="sum", scale=10)"""


"""Write a recursive function recursive_search(data, target) that searches for a element inside a nested list of arbitrary depth and returns True if found, otherwise False"""
"""def recursive_search(data, target):
    for item in data:

        if isinstance(item, list):
            if recursive_search(item, target):
                return True

        elif item == target:
            return True

    return False
data = [1, 2, [3, 4, [5, 6]], 7]
print(recursive_search(data, 5))"""

"""Bank Account Hierarchy
Implement a class structure demonstrating Encapsulation and Inheritance:
BankAccount : Base class with private attribute 
__balance , methods 
deposit() , 
withdraw() , and getter
get_balance() . Raise 
InsufficientFundsError if withdrawal exceeds balance.
SavingsAccount : Derived class with 
interest_rate attribute and a method """

"""class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient balance")
        self.__balance = self.__balance - amount

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)

account = SavingsAccount(1000, 5)

account.deposit(500)
account.withdraw(200)
account.apply_interest()

print("Balance:", account.get_balance())"""

"""E-Commerce Shopping Cart System
Build an interactive shopping cart system using OOP principles:
Item class: Stores 
name , 
price , and  .
quantity . Includes a method 
get_total_price() .
ShoppingCart class: Contains a collection of 
Item objects. Implements methods to 
remove_item() , and 
calculate_grand_total() with tax application."""

"""class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                break

    def calculate_grand_total(self, tax):
        total = 0

        for item in self.items:
            total = total + item.get_total_price()

        total = total + (total * tax / 100)

        return total


# Example
item1 = Item("Pen", 10, 2)
item2 = Item("Book", 100, 3)

cart = ShoppingCart()

cart.add_item(item1)
cart.add_item(item2)

print("Grand Total:", cart.calculate_grand_total(10))

cart.remove_item("Pen")

print("After removing Pen:", cart.calculate_grand_total(10))"""


""" Shape Polymorphism & Area Calculator
Create an abstract interface 
Shape with an abstract method 
Circle , 
Rectangle , and 
Triangle . Write a function 
and computes total combined area using polymorphism.
add_item() ,
area() . Implement concrete subclasses
total_area(shapes) that accepts a list of shapes"""

"""from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def total_area(shapes):
    total = 0

    for shape in shapes:
        total = total + shape.area()

    return total


# Example
circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 4)

shapes = [circle, rectangle, triangle]

print("Total Area:", total_area(shapes))"""

#-------------------------------------------------

"""Nested JSON Key Extraction
Write a recursive function 
extract_nested_keys(d, target_key) that searches through arbitrary nested dictionary
structures (like JSON responses) and collects all instances matching a specific key."""

"""def extract_nested_keys(d, target_key):
    result = []

    for key, value in d.items():

        if key == target_key:
            result.append(value)

        if isinstance(value, dict):
            result = result + extract_nested_keys(value, target_key)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    result = result + extract_nested_keys(item, target_key)

    return result

data = {
    "name": "John",
    "details": {
        "age": 25,
        "name": "David"
    },
    "address": {
        "city": "Bangalore",
        "contact": {
            "name": "Alex"
        }
    }
}

print(extract_nested_keys(data, "name"))"""

""" Run-Length Encoding & Compression
Write a function 
Level 1 — Intermediate
compress_string(s) that performs basic run-length encoding on an alphanumeric string (e.g.,
"aabcccccaaa" becomes 
"a2b1c5a3" ). If the compressed string is not smaller than the original, return the original string."""

"""def compress_string(s):
    d = ""
    count = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            d += s[i] + str(count)
            count = 1

    d += s[-1] + str(count)

    if len(d) < len(s):
        return d
    else:
        return s

print(compress_string("aabcccccaaa"))"""

""" Longest Consecutive Sequence Finder
Write a function 
longest_consecutive(nums) that takes an unsorted list of integers and finds the length of the longest
consecutive elements sequence in O(n) time using sets"""
"""def longest_consecutive(nums):
    numbers = set(nums)
    longest = 0

    for num in numbers:
        if num - 1 not in numbers:
            count = 1
            current = num

            while current + 1 in numbers:
                current += 1
                count += 1

            if count > longest:
                longest = count

    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))"""

"""Sliding Window Moving Average
Write a function 
moving_average(data, window_size) that computes the simple moving average over a numerical list
using a sliding window approach. Return a list of averages rounded to 2 decimal places."""

"""def moving_average(data, window_size):
    result = []

    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        average = sum(window) / window_size
        result.append(round(average, 2))

    return result

print(moving_average([1, 2, 3, 4, 5], 3))"""

""" Pascal's Triangle Generator
Write a function 
generate_pascals_triangle(num_rows) that outputs the first N rows of Pascal's Triangle as a nested
list of integers"""

"""def generate_pascals_triangle(num_rows):
    triangle = []

    for i in range(num_rows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
print(generate_pascals_triangle(5))"""

""" Valid Anagram & Grouping Engine
Write a function 
group_anagrams(words) that takes a list of strings and groups anagrams together into a dictionary where
sorted string representations act as unique keys."""

"""def group_anagrams(words):
    groups = {}

    for word in words:
        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return groups

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))"""

""" Tabular CSV-like Dict Alignment
Write a function 
align_records(records) that takes an inconsistent list of dict records (where some keys may be missing
across entries) and standardizes them into a uniform dictionary with default values for missing keys."""

"""def align_records(records):
    all_keys = set()
    for record in records:
        for key in record:
            all_keys.add(key)
    result = []
    for record in records:
        new_record = {}
        for key in all_keys:
            if key in record:
                new_record[key] = record[key]
            else:
                new_record[key] = None

        result.append(new_record)
    return result

records = [
    {"name": "John", "age": 25},
    {"name": "Alice", "city": "Bangalore"},
    {"name": "Bob", "age": 30}
]
print(align_records(records))"""

""" Matrix Multiplication (Pure Python)
Write a function 
matrix_multiply(A, B) that performs matrix multiplication between two 2D lists. Validate that column
dimensions of A equal row dimensions of B; otherwise raise a custom 
DimensionMismatchError ."""

"""class DimensionMismatchError(Exception):
    pass

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise DimensionMismatchError("Matrix dimensions do not match")

    result = []

    for i in range(len(A)):
        row = []

        for j in range(len(B[0])):
            total = 0

            for k in range(len(B)):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print(matrix_multiply(A, B))"""

""" Nested JSON Key Extraction
Write a recursive function 
extract_nested_keys(d, target_key) that searches through arbitrary nested dictionary
structures (like JSON responses) and collects all instances matching a specific key."""
"""def extract_nested_keys(data, target_key):
    result = []

    if isinstance(data, dict):
        for key, value in data.items():

            if key == target_key:
                result.append(value)

            if isinstance(value, (dict, list)):
                result.extend(extract_nested_keys(value, target_key))

    elif isinstance(data, list):
        for item in data:
            result.extend(extract_nested_keys(item, target_key))

    return result


data = {
    "name": "John",
    "details": {
        "name": "Smith",
        "age": 25
    }
}
print(extract_nested_keys(data, "name"))"""

""" Custom Pivot Table Simulation
Write a function pivot_summary(data, group_by_col, value_col) that takes a list of dictionary rows, groups values by
group_by_col , and aggregates the sum, average, and count for 
value_col ."""
"""def pivot_summary(data, group_by_col, value_col):
    groups = {}

    for row in data:
        group = row[group_by_col]
        value = row[value_col]

        if group not in groups:
            groups[group] = []

        groups[group].append(value)

    result = {}

    for group, values in groups.items():
        result[group] = {
            "sum": sum(values),
            "average": sum(values) / len(values),
            "count": len(values)
        }

    return result


data = [
    {"department": "IT", "salary": 50000},
    {"department": "IT", "salary": 60000},
    {"department": "HR", "salary": 40000}
]

print(pivot_summary(data, "department", "salary"))"""

"""Priority Task Queue (Min-Heap / Dict Logic)
Implement a priority task dispatcher function process_tasks(tasks) where each task is a dict with 
{"name": str,
"priority": int} . Process and return task names in order from highest priority (lowest integer value) to lowest."""

"""def process_tasks(tasks):
    tasks.sort(key=lambda x: x["priority"])

    result = []

    for task in tasks:
        result.append(task["name"])

    return result


tasks = [
    {"name": "Task A", "priority": 3},
    {"name": "Task B", "priority": 1},
    {"name": "Task C", "priority": 2}
]

print(process_tasks(tasks))"""

"""Create a decorator function 
@time_execution that logs the elapsed runtime in milliseconds for any function it decorates,
printing execution metadata automatically upon function completion."""

"""import time


def time_execution(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        time_taken = (end - start) * 1000

        print("Function:", func.__name__)
        print("Time:", time_taken, "ms")

        return result

    return wrapper


@time_execution
def test_function():
    time.sleep(1)


test_function()"""

"""Lazy Evaluation File Batcher (Generator)
Write a generator function 
chunk_file_reader(filepath, chunk_size=100) that reads a large file lazily line-by-line and
yields list chunks of size 
chunk_size to conserve memory."""

"""def chunk_file_reader(filepath, chunk_size=100):

    with open(filepath, "r") as file:

        chunk = []

        for line in file:
            chunk.append(line)

            if len(chunk) == chunk_size:
                yield chunk
                chunk = []

        if len(chunk) > 0:
            yield chunk"""

""" Data Validation Decorator
Create a decorator 
{"val": float} ) and raises a 
@enforce_types(type_schema) that checks arguments passed to a function against a schema
dictionary (e.g. 
TypeError if invalid data types are supplied."""

"""def enforce_types(type_schema):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for name, value in kwargs.items():

                if name in type_schema:
                    if not isinstance(value, type_schema[name]):
                        raise TypeError(
                            name + " must be " + str(type_schema[name])
                        )

            return func(*args, **kwargs)

        return wrapper

    return decorator


@enforce_types({"val": float})
def show_value(val):
    print(val)


show_value(val=10.5)"""

"""Custom Memoization Decorator
Implement a caching decorator 
@memoize that stores previously computed function results in a dictionary cache to speed up
expensive recursive algorithms like computing Fibonacci numbers."""

"""def memoize(func):
    cache = {}

    def wrapper(n):

        if n in cache:
            return cache[n]

        result = func(n)

        cache[n] = result

        return result

    return wrapper


@memoize
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))"""

"""Custom Array / Matrix Container Class
Design a class 
Array2D that wraps a flat list and dimensions 
Overload 
__getitem__ and 
(rows, cols) :
__setitem__ to allow tuple indexing like 
Include a 
reshape(new_rows, new_cols) method that returns a re-indexed 
"""
"""class Array2D:

    def __init__(self, data, rows, cols):
        self.data = data
        self.rows = rows
        self.cols = cols

    def __getitem__(self, index):
        row, col = index
        position = row * self.cols + col
        return self.data[position]

    def __setitem__(self, index, value):
        row, col = index
        position = row * self.cols + col
        self.data[position] = value

    def reshape(self, new_rows, new_cols):
        if new_rows * new_cols != len(self.data):
            raise ValueError("Cannot reshape")

        return Array2D(self.data.copy(), new_rows, new_cols)


arr = Array2D([1, 2, 3, 4, 5, 6], 2, 3)

print(arr[1, 2])

arr[1, 2] = 10

print(arr[1, 2])

new_arr = arr.reshape(3, 2)

print(new_arr[2, 1])"""

"""Data Pipeline Filter Chain
Build a modular class structure for a data pipeline:
BasePipelineStep : Abstract class with a method 
process(data) .
Implement concrete steps: 
FillMissingStep(default_val) , 
FilterOutliersStep(min_val, max_val) .
Pipeline : Class that chains steps and runs 
execute(data) sequentially""".


"""from abc import ABC, abstractmethod


class BasePipelineStep(ABC):

    @abstractmethod
    def process(self, data):
        pass


class FillMissingStep(BasePipelineStep):

    def __init__(self, default_val):
        self.default_val = default_val

    def process(self, data):
        return [
            self.default_val if x is None else x
            for x in data
        ]


class ScaleStep(BasePipelineStep):

    def __init__(self, factor):
        self.factor = factor

    def process(self, data):
        return [x * self.factor for x in data]


class FilterOutliersStep(BasePipelineStep):

    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def process(self, data):
        return [
            x for x in data
            if self.min_val <= x <= self.max_val
        ]


class Pipeline:

    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def execute(self, data):
        for step in self.steps:
            data = step.process(data)

        return data


pipeline = Pipeline()

pipeline.add_step(FillMissingStep(0))
pipeline.add_step(ScaleStep(2))
pipeline.add_step(FilterOutliersStep(0, 10))

data = [1, None, 3, 20]

print(pipeline.execute(data))"""

"""Bank Transaction Ledger with Properties
Implement a class 
AccountLedger using Python `@property` syntax:
Maintain a private transaction history log `__transactions`.
Read-only properties: 
balance (computed dynamically) and transaction_count 
Prevent direct mutation of ledger entries from outside the class.
"""
"""class AccountLedger:

    def __init__(self):
        self.__transactions = []

    def deposit(self, amount):
        self.__transactions.append(amount)

    def withdraw(self, amount):
        self.__transactions.append(-amount)

    @property
    def balance(self):
        return sum(self.__transactions)

    @property
    def transaction_count(self):
        return len(self.__transactions)


account = AccountLedger()

account.deposit(1000)
account.withdraw(200)
account.deposit(500)

print(account.balance)
print(account.transaction_count)"""

""" Polymorphic File Exporter System
Build a data export module for dictionary datasets:
Abstract class 
DataExporter with abstract method 
Subclasses: 
export(data, filepath) .
CSVExporter (formats as comma-separated values) and 
JSONExporter (formats as indented JSON
string).
Class Factory: 
ExporterFactory.get_exporter(format_type) that returns appropriate instances."""

"""from abc import ABC, abstractmethod
import csv
import json


class DataExporter(ABC):

    @abstractmethod
    def export(self, data, filepath):
        pass


class CSVExporter(DataExporter):

    def export(self, data, filepath):

        with open(filepath, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=data[0].keys()
            )

            writer.writeheader()
            writer.writerows(data)


class JSONExporter(DataExporter):

    def export(self, data, filepath):

        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)


class ExporterFactory:

    @staticmethod
    def get_exporter(format_type):

        if format_type == "csv":
            return CSVExporter()

        elif format_type == "json":
            return JSONExporter()

        else:
            raise ValueError("Unknown format")


data = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30}
]

exporter = ExporterFactory.get_exporter("json")
exporter.export(data, "data.json")"""

""" Custom Mini-DataFrame Class (Pre-Pandas Master Task)
Build a 
MiniDataFrame class storing tabular data as a dictionary of column lists (e.g. 
[50000, 60000]} ):
Methods:
info() : Displays column names, non-null counts, and data types.
{"age": [25, 30], "salary":
describe() : Computes count, mean, min, and max for each numerical column.
filter_by(col_name, predicate_func) : Returns a new filtered 
MiniDataFrame instance."""

"""class MiniDataFrame:

    def __init__(self, data):
        self.data = data

    def info(self):

        for column in self.data:
            values = self.data[column]

            count = 0

            for value in values:
                if value is not None:
                    count += 1

            data_type = type(values[0]).__name__

            print(
                column,
                "Non-null:", count,
                "Type:", data_type
            )

    def describe(self):

        result = {}

        for column in self.data:

            values = self.data[column]

            if isinstance(values[0], (int, float)):

                result[column] = {
                    "count": len(values),
                    "mean": sum(values) / len(values),
                    "min": min(values),
                    "max": max(values)
                }

        return result

    def filter_by(self, col_name, predicate_func):

        indexes = []

        for i in range(len(self.data[col_name])):

            if predicate_func(self.data[col_name][i]):
                indexes.append(i)

        new_data = {}

        for column in self.data:

            new_data[column] = []

            for i in indexes:
                new_data[column].append(self.data[column][i])

        return MiniDataFrame(new_data)


data = {
    "age": [25, 30, 35],
    "salary": [30000, 40000, 50000]
}

df = MiniDataFrame(data)

df.info()

print(df.describe())

new_df = df.filter_by("age", lambda x: x > 25)

print(new_df.data)"""

"""GroupBy & Aggregate Engine
Add advanced grouping capability to the 
MiniDataFrame class:
Implement a method 
groupby(col_name) that returns a custom 
Implement aggregation methods on 
GroupedData object.
GroupedData such as 
sum() and 
mean() that calculate group-level summary
metrics.
"""

"""class GroupedData:

    def __init__(self, data, column):
        self.data = data
        self.column = column

    def sum(self):

        result = {}

        for row in self.data:
            group = row[self.column]

            if group not in result:
                result[group] = 0

            result[group] += row["value"]

        return result

    def mean(self):

        groups = {}
        result = {}

        for row in self.data:

            group = row[self.column]

            if group not in groups:
                groups[group] = []

            groups[group].append(row["value"])

        for group in groups:
            result[group] = sum(groups[group]) / len(groups[group])

        return result



class MiniDataFrame:

    def __init__(self, data):
        self.data = data

    def groupby(self, col_name):

        return GroupedData(self.data, col_name)


data = [
    {"department": "IT", "value": 100},
    {"department": "IT", "value": 200},
    {"department": "HR", "value": 300},
    {"department": "HR", "value": 100}
]

df = MiniDataFrame(data)

grouped = df.groupby("department")

print(grouped.sum())
print(grouped.mean())"""


