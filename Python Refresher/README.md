# 🐍 Python Basics Notes

> A quick revision guide covering the most important Python fundamentals.

---

# Table of Contents

1. Variables
2. Data Types
3. Operators
4. Conditional Statements (if-else)
5. Loops
6. Functions
7. Modules
8. Packages

---

# 1. Variables

Variables store data in memory.

## Syntax

```python
name = "Tahmid"
age = 20
cgpa = 3.85
is_student = True
```

Python is dynamically typed, so you don't need to specify the data type.

```python
x = 10
x = "Hello"
```

---

# Variable Naming Rules

✅ Valid

```python
student_name
studentName
student1
_age
```

❌ Invalid

```python
1student
student-name
class
```

---

# Multiple Assignment

```python
a, b, c = 10, 20, 30

x = y = z = 100
```

---

# Constants

Python has no true constants.

Convention:

```python
PI = 3.1416
MAX_SIZE = 100
```

---

# 2. Data Types

## Numeric

```python
a = 10        # int
b = 3.14      # float
c = 2 + 5j    # complex
```

---

## Boolean

```python
flag = True
status = False
```

---

## String

```python
name = "Python"
```

Access characters

```python
print(name[0])
print(name[-1])
```

Slicing

```python
print(name[0:3])
print(name[:4])
print(name[2:])
```

---

## List

Mutable collection.

```python
numbers = [1,2,3,4]
```

Methods

```python
append()

insert()

extend()

remove()

pop()

sort()

reverse()
```

---

## Tuple

Immutable collection.

```python
point = (10,20)
```

---

## Set

Unique unordered values.

```python
nums = {1,2,3}
```

Methods

```python
add()

remove()

discard()
```

---

## Dictionary

Key-value pair.

```python
student = {
    "name":"Tahmid",
    "age":20
}
```

Access

```python
student["name"]

student.get("age")
```

Loop

```python
for key, value in student.items():
    print(key, value)
```

---

# Type Conversion

```python
int()

float()

str()

list()

tuple()

set()
```

Example

```python
x = int("100")
```

---

# 3. Operators

## Arithmetic

| Operator | Meaning |
|----------|---------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| // | Floor Division |
| % | Modulus |
| ** | Power |

Example

```python
a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
```

---

## Comparison

```python
>

<

>=

<=

==

!=
```

---

## Logical

```python
and

or

not
```

---

## Assignment

```python
+=

-=

*=

/=

%=

**=
```

---

## Membership

```python
in

not in
```

Example

```python
print("P" in "Python")
```

---

## Identity

```python
is

is not
```

---

# 4. Conditional Statements

## if

```python
if age >= 18:
    print("Adult")
```

---

## if-else

```python
if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

---

## if-elif-else

```python
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("Fail")
```

---

## Nested if

```python
if age >= 18:
    if age >= 60:
        print("Senior Citizen")
```

---

## Ternary Operator

```python
result = "Pass" if marks >= 40 else "Fail"
```

---

# 5. Loops

## for Loop

```python
for i in range(5):
    print(i)
```

---

## range()

```python
range(stop)

range(start, stop)

range(start, stop, step)
```

Examples

```python
range(5)

range(1,6)

range(0,10,2)
```

---

## while Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## break

```python
for i in range(10):
    if i == 5:
        break
```

---

## continue

```python
for i in range(5):
    if i == 2:
        continue
```

---

## pass

```python
for i in range(5):
    pass
```

---

# 6. Functions

Function definition

```python
def greet():
    print("Hello")
```

Calling

```python
greet()
```

---

## Parameters

```python
def add(a, b):
    return a+b
```

---

## Default Parameter

```python
def greet(name="Guest"):
    print(name)
```

---

## Keyword Arguments

```python
greet(name="Tahmid")
```

---

## Return Statement

```python
def square(x):
    return x*x
```

---

## Lambda Function

```python
square = lambda x: x*x
```

---

## Built-in Functions

```python
len()

sum()

max()

min()

sorted()

type()

input()

print()
```

---

# Variable Scope

Global

```python
x = 10
```

Local

```python
def fun():
    x = 5
```

---

# 7. Modules

A module is a Python file containing reusable code.

Import

```python
import math
```

Use

```python
math.sqrt(25)
```

---

Import specific function

```python
from math import sqrt

sqrt(25)
```

---

Import alias

```python
import numpy as np
```

---

Useful Built-in Modules

```python
math

random

os

sys

datetime

time

statistics

collections
```

---

# 8. Packages

A package is a collection of modules.

Install

```bash
pip install package_name
```

Examples

```bash
pip install numpy

pip install pandas

pip install matplotlib

pip install scikit-learn
```

Import

```python
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
```

---

# Common Built-in Functions

```python
len()

sum()

max()

min()

round()

abs()

sorted()

type()

id()

range()

enumerate()

zip()
```

---

# Important String Methods

```python
upper()

lower()

title()

capitalize()

strip()

replace()

split()

join()

find()

count()
```

---

# Important List Methods

```python
append()

extend()

insert()

remove()

pop()

sort()

reverse()

clear()
```

---

# Important Dictionary Methods

```python
keys()

values()

items()

get()

update()

pop()
```

---

# Revision Checklist

- [ ] Variables
- [ ] Data Types
- [ ] Type Conversion
- [ ] Operators
- [ ] if
- [ ] if-else
- [ ] if-elif-else
- [ ] for Loop
- [ ] while Loop
- [ ] break
- [ ] continue
- [ ] pass
- [ ] Functions
- [ ] Parameters
- [ ] Return
- [ ] Lambda
- [ ] Scope
- [ ] Modules
- [ ] Packages
- [ ] Built-in Functions
- [ ] String Methods
- [ ] List Methods
- [ ] Dictionary Methods

---

# What's Next?

After mastering these topics, move on to:

1. Exception Handling
2. File Handling
3. Object-Oriented Programming (OOP)
4. List/Dictionary Comprehensions
5. Iterators & Generators
6. Decorators
7. Context Managers
8. Regular Expressions
9. NumPy
10. Pandas
11. Matplotlib
12. Scikit-Learn
13. Machine Learning
