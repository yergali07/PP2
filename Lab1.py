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

# 12. Data Types: Getting the Data Type
x = 5
print(type(x))

# 13. Python Numbers: Python Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# 13. Python Numbers: Int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# 13. Python Numbers: Float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# 13. Python Numbers: Complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# 13. Python Numbers: Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# 13. Python Numbers: Random Number
import random

print(random.randrange(1, 10))

# 14. Python Casting: Specify a Variable Type
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# 15. Python Strings: Strings
print("Hello")
print('Hello')

# 15. Python Strings: Quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# 15. Python Strings: Assign String to a Variable
a = "Hello"
print(a)

# 15. Python Strings: Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# 15. Python Strings: Strings are Arrays
a = "Hello, World!"
print(a[1])

# 15. Python Strings: Looping Through a String
for x in "banana":
  print(x)

# 15. Python Strings: String Length
a = "Hello, World!"
print(len(a))

# 15. Python Strings: Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# 15. Python Strings: Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# 16. Slicing Strings: Slicing
b = "Hello, World!"
print(b[2:5])

# 16. Slicing Strings: Slice From the Start
b = "Hello, World!"
print(b[:5])

# 16. Slicing Strings: Slice To the End
b = "Hello, World!"
print(b[2:])

# 16. Slicing Strings: Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# 17. Modify Strings: Upper Case
a = "Hello, World!"
print(a.upper())

# 17. Modify Strings: Lower Case
a = "Hello, World!"
print(a.lower())

# 17. Modify Strings: Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# 17. Modify Strings: Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# 17. Modify Strings: Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# 18. Concatenate Strings: String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# 19. Format Strings: F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# 19. Format Strings: Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# 20. Escape Characters: Escape Characters
txt = "We are the so-called \"Vikings\" from the north."

# 21. String Methods: String Methods

#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isascii()	Returns True if all characters in the string are ascii characters
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning