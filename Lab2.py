# 22. Python Booleans: Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# 22. Python Booleans: Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# 22. Python Booleans: Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# 22. Python Booleans: Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# 22. Python Booleans: Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int))

# 23. Python Operators: Python Operators
print(10 + 5)

# 23. Python Operators: Operator Precedence
print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

print(5 + 4 - 7 + 3)

# 24. Python Lists: List
thislist = ["apple", "banana", "cherry"]
print(thislist)

# 24. Python Lists: Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# 24. Python Lists: List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# 24. Python Lists: List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

# 24. Python Lists: type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# 24. Python Lists: The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# 24. Python Lists: Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# 24. Python Lists: Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# 24. Python Lists: Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

# 24. Python Lists: Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# 24. Python Lists: Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# 24. Python Lists: Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# 24. Python Lists: Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# 24. Python Lists: Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# 24. Python Lists: Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# 24. Python Lists: Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# 24. Python Lists: Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# 24. Python Lists: Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# 24. Python Lists: Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# 24. Python Lists: Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# 24. Python Lists: The del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

# 24. Python Lists: The clear() method
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# 24. Python Lists: Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# 24. Python Lists: Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# 24. Python Lists: Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# 24. Python Lists: List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Without list comprehension    
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# 24. Python Lists: The syntax
#newlist = [expression for item in iterable if condition == True]

# 24. Python Lists: Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# 24. Python Lists: Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# 24. Python Lists: Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# 24. Python Lists: Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# 24. Python Lists: Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# 24. Python Lists: Copy a List
# Using the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Using the list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Using the slicing syntax
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# 24. Python Lists: Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# 25. Python Tuples: Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# 25. Python Tuples: Tuple Items
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# 25. Python Tuples: Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# 25. Python Tuples: Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# 25. Python Tuples: Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

# 25. Python Tuples: type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# 25. Python Tuples: The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# 25. Python Tuples: Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# 25. Python Tuples: Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# 25. Python Tuples: Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# 25. Python Tuples: Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# 25. Python Tuples: Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# 25. Python Tuples: Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# 25. Python Tuples: Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# 25. Python Tuples: Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# 25. Python Tuples: Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# 25. Python Tuples: Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# 25. Python Tuples: Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# 25. Python Tuples: Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# 25. Python Tuples: Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# 25. Python Tuples: Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# 25. Python Tuples: Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# 26. Python Sets: Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# 26. Python Sets: Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# 26. Python Sets: Set Length
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# 26. Python Sets: Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# 26. Python Sets: The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# 26. Python Sets: Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

# 26. Python Sets: Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# 26. Python Sets: Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# 26. Python Sets: Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# 26. Python Sets: Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# 26. Python Sets: Empty Set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

# 26. Python Sets: Loop Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# 26. Python Sets: Join Sets
# Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#or

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# 26. Python Sets: Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# or

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# 26. Python Sets: Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# 26. Python Sets: The update() Method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# 26. Python Sets: Keep ONLY the Duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# or

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# 26. Python Sets: intersection_update() Method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# 26. Python Sets: Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# or

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# 26. Python Sets: difference_update() Method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# 26. Python Sets: Symmetric Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# or

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# 26. Python Sets: symmetric_difference_update() Method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

# 27. Python Dictionaries: Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# 27. Python Dictionaries: Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# 27. Python Dictionaries: Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# 27. Python Dictionaries: Dictionary Length
print(len(thisdict))

# 27. Python Dictionaries: Dictionary Items - Data Types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# 27. Python Dictionaries: type()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# 27. Python Dictionaries: The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# 27. Python Dictionaries: Accessing Items
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


x = thisdict.get("model")

# 27. Python Dictionaries: Get Keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# 27. Python Dictionaries: Get Values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# 27. Python Dictionaries: Get Items
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# 27. Python Dictionaries: Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# 27. Python Dictionaries: Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# 27. Python Dictionaries: Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# 27. Python Dictionaries: Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# 27. Python Dictionaries: Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# 27. Python Dictionaries: Loop Through a Dictionary
for x in thisdict:
  print(x)

# 27. Python Dictionaries: Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# 27. Python Dictionaries: Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# or

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# 27. Python Dictionaries: Accessing Nested Dictionaries
print(myfamily["child2"]["name"])

# 27. Python Dictionaries: Loop Through a Nested Dictionary
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

# 28. Python If...Else: If Statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

# 28. Python If...Else: Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# 28. Python If...Else: Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# 28. Python If...Else: Short Hand If
if a > b: print("a is greater than b")

# 28. Python If...Else: Short Hand If...Else
a = 2
b = 330
print("A") if a > b else print("B")

# 28. Python If...Else: And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# 28. Python If...Else: Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# 28. Python If...Else: Not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# 28. Python If...Else: Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# 29. Python If...Else: The pass Statement
a = 33
b = 200

if b > a:
  pass

# 30. Python While Loops: While Loop
i = 1
while i < 6:
  print(i)
  i += 1

# 30. Python While Loops: The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# 30. Python While Loops: The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# 30. Python While Loops: The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# 31. Python For Loops: For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# 31. Python For Loops: Looping Through a String
for x in "banana":
  print(x)

# 31. Python For Loops: The break Statement
for x in "banana":
  print(x)

# 31. Python For Loops: The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# 31. Python For Loops: The range() Function
for x in range(6):
  print(x)

# 31. Python For Loops: Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# 31. Python For Loops: Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# 31. Python For Loops: The pass Statement
for x in [0, 1, 2]:
  pass
