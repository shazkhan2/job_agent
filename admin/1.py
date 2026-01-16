# unit = "cm"
# def calc_rect_area(length, width):
#     """Calculate the area of a rectangle."""
#     area = length * width
#     print(area)

# result = calc_rect_area(5, 10)
# print (result, unit)
# Namespace
# return statement
# Assigning return values to variables
"""what would be the output of the following code snippet?
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
print(greet("Bob"))"""

"""Predict the output of the following code snippet:
def add(a, b):
    return a + b

result = add(5, 10)
print(result)
print(add(result, 20))"""

"""What will this code print
def compute(a, b):
    result = a * b
    if result > 10:
        return result - 3
    else:
        return result + 4

print(compute(3, 2))
print(compute(5, 3))"""

"""This function uses a global variable. What will be the output?
counter = 10

def increment(value):
    global counter
    counter += value
    return counter

print(increment(5))
print(increment(3))
print(counter)"""

"""Decorators"""
# def change_case(func):
#     def daddy():
#         return func().upper()
#     return daddy

# @change_case
# def writing():
#     return "hello dear"
# print(writing())


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")
        
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 5)
# dog1.bark()
# dog2.bark()
# def my_function(*num):
#   return sum(num)

# print(my_function(1,2,3))
# def countdown(n):
#   if n <= 0:
#     print("Done!")
#   else:
#     print(n)
#     countdown(n - 1)

# countdown(5)

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))