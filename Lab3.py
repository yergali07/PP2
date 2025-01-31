# 32. Python Functions: Creating a Function
def my_function():
  print("Hello from a function")

# 32. Python Functions: Calling a Function
def my_function():
  print("Hello from a function")

my_function()

# 32. Python Functions: Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# 32. Python Functions: Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# 32. Python Functions: Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# 32. Python Functions: Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# 32. Python Functions: Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# 32. Python Functions: Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# 32. Python Functions: Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# 32. Python Functions: Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# 32. Python Functions: The pass Statement
def myfunction():
  pass

# 32. Python Functions: Positional Arguments
def my_function(x, /):
  print(x)

my_function(3)

# 32. Python Functions: Keyword-Only Arguments
def my_function(*, x):
  print(x)

my_function(x = 3)

# 32. Python Functions: Combining Positional and Keyword Arguments
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# 32. Python Functions: Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

# 33. Python Lambda: Syntax
x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# 33. Python Lambda: Why Use Lambda Functions?
def myfunc(n):
  return lambda a : a * n


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# 34. Python Arrays: Arrays
cars = ["Ford", "Volvo", "BMW"]

# 34. Python Arrays: Access the Elements of an Array
x = cars[0]

# 34. Python Arrays: Modify the Value of an Array
cars[0] = "Toyota"

# 34. Python Arrays: The Length of an Array
x = len(cars)

# 34. Python Arrays: Looping Array Elements
for x in cars:
  print(x)

# 34. Python Arrays: Adding Array Elements
cars.append("Honda")

# 34. Python Arrays: Removing Array Elements
cars.pop(1)

cars.remove("Volvo")

# 35. Python Classes and Objects: Create a Class
class MyClass:
  x = 5

# 35. Python Classes and Objects: Create Object
p1 = MyClass()
print(p1.x)

# 35. Python Classes and Objects: The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# 35. Python Classes and Objects: The __str__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# 35. Python Classes and Objects: Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# 35. Python Classes and Objects: The self Parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# 35. Python Classes and Objects: Modify Object Properties
p1.age = 40

# 35. Python Classes and Objects: Delete Object Properties
del p1.age

# 35. Python Classes and Objects: Delete Objects
del p1

# 35. Python Classes and Objects: The pass Statement
class Person:
  pass

# 36. Python Inheritance: Create a Parent Class 
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# 36. Python Inheritance: Create a Child Class
class Student(Person):
  pass


x = Student("Mike", "Olsen")
x.printname()

# 36. Python Inheritance: Add the __init__() Function
#class Student(Person):
#  def __init__(self, fname, lname):
    #add properties etc.
    
# 36. Python Inheritance: Use the super() Function
#class Student(Person):
#  def __init__(self, fname, lname):
#    super().__init__(fname, lname)

# 36. Python Inheritance: Add Properties
#class Student(Person):
#  def __init__(self, fname, lname):
#    super().__init__(fname, lname)
#    self.graduationyear = 2019

# 36. Python Inheritance: Add Methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
