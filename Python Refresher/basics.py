# ======================================================
# PYTHON ONE-SHOT SYNTAX REVISION
# Topics:
# Variables, Data Types, Operators, if-else, Loops,
# Functions, Modules, Packages
# ======================================================

# ---------- MODULES ----------
import math
import random
from datetime import datetime

# ---------- VARIABLES ----------
name = "Tahmid"
age = 20
cgpa = 3.85
is_student = True

print("===== VARIABLES =====")
print(name, age, cgpa, is_student)

# ---------- DATA TYPES ----------
integer = 100
floating = 10.5
string = "Python"
boolean = False

my_list = [10, 20, 30]
my_tuple = (1, 2, 3)
my_set = {5, 6, 7}
my_dict = {"name": "Tahmid", "dept": "CSE"}

print("\n===== DATA TYPES =====")
print(type(integer))
print(type(floating))
print(type(string))
print(type(boolean))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dict))

# ---------- OPERATORS ----------
a = 15
b = 4

print("\n===== OPERATORS =====")

# Arithmetic
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a**b)

# Comparison
print(a > b)
print(a < b)
print(a == b)
print(a != b)

# Logical
print(a > 10 and b < 10)
print(a > 20 or b < 10)
print(not is_student)

# Assignment
x = 5
x += 3
x *= 2
print("Assignment Result:", x)

# Membership
print("Py" in string)

# Identity
list1 = [1, 2]
list2 = list1
print(list1 is list2)

# ---------- IF ELSE ----------
print("\n===== IF ELSE =====")

marks = 83

if marks >= 80:
    print("Grade A+")
elif marks >= 70:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail")

# ---------- LOOPS ----------
print("\n===== FOR LOOP =====")

for i in range(1, 6):
    print(i)

print("\n===== WHILE LOOP =====")

count = 1
while count <= 5:
    print(count)
    count += 1

print("\n===== BREAK =====")

for i in range(10):
    if i == 5:
        break
    print(i)

print("\n===== CONTINUE =====")

for i in range(6):
    if i == 3:
        continue
    print(i)

# ---------- FUNCTIONS ----------
print("\n===== FUNCTIONS =====")


def greet(name):
    return f"Hello {name}"


def square(x):
    return x * x


def add(a, b=10):
    return a + b


print(greet("Tahmid"))
print(square(8))
print(add(5))
print(add(5, 20))

# ---------- MODULE USAGE ----------
print("\n===== MODULES =====")

print("Square Root:", math.sqrt(64))
print("Pi:", math.pi)
print("Random Number:", random.randint(1, 100))
print("Current Time:", datetime.now())

# ---------- BUILT-IN FUNCTIONS ----------
print("\n===== BUILT-IN FUNCTIONS =====")

numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers, reverse=True))

# ---------- STRING METHODS ----------
print("\n===== STRING METHODS =====")

language = "python programming"

print(language.upper())
print(language.lower())
print(language.title())
print(language.replace("python", "Java"))
print(language.split())

# ---------- LIST METHODS ----------
print("\n===== LIST METHODS =====")

nums = [1, 2, 3]
nums.append(4)
nums.extend([5, 6])
nums.insert(0, 100)
nums.remove(2)
nums.pop()

print(nums)

# ---------- DICTIONARY ----------
print("\n===== DICTIONARY =====")

student = {"name": "Tahmid", "age": 20}

student["cgpa"] = 3.8

for key, value in student.items():
    print(key, ":", value)

# ---------- PACKAGE EXAMPLE ----------
# pip install numpy
# pip install pandas

# import numpy as np
# import pandas as pd

print("\nPackages are installed using:")
print("pip install package_name")

# ---------- MAIN ----------
print("\n===== PROGRAM FINISHED =====")
