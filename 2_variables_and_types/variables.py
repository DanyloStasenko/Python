# Lesson 2. "Variables and Types"
# https://www.learnpython.org/en/Variables_and_Types

# 1. Declare int
myint = 7
print(myint)

# 2. Declare float
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# 2. Declare string with single/double quotes
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

# 3. Adding integers and strings
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# 4. Declaring few values
a, b = 3, 4
print(a,b)

# 5.Mixing operators between numbers and strings is not supported:
# This will not work!
# one = 1
# two = 2
# hello = "hello"
#
# print(one + two + hello)      TypeError: unsupported operand type(s) for +: 'int' and 'str'

