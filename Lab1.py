# 1. HOME
print('Hello, World!')

# 3. Get started: The Python version
import sys

print(sys.version)

# 4. Syntax: Python indentation
if 5 > 2:
  print("Five is greater than two!")

# 4. Syntax: Python variables
x = 5
y = "Hello, World!"

# 4. Syntax: Python comments
#This is a comment.
print("Hello, World!")

# 5. Comments: Multi Line Comments
#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# 6. Variables: Creating Variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# 6. Variables: Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# 6. Variables: Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

# 6. Variables: Single or Double Quotes?
x = "John"
# is the same as
x = 'John'

# 6. Variables: Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a

# 7. Variable Names: Legal Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# 7. Variable Names: Illegal Variable Names
#2myvar = "John"
#my-var = "John"
#my var = "John"

# 7. Variable Names: Multi Words Variable Names
myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

# 8. Assign Multiple Values: Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# 8. Assign Multiple Values: One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# 8. Assign Multiple Values: Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# 9. Output Variables: Output Variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

# 10. Global Variables: Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# 11. Global Keyword: The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
