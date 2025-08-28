print("Hello World")


"""
import sys
print(sys.version)
"""

if 5 > 2:      
    print("five is greater than two")
    if 2 < 5:
        print("two is smaller than five")

# Remember that variable names are case-sensitive

# x = "5"
x='5'
X='1'
X=3
y = "Hello World"
x = int(5)
print(x,y)
print(type(x))
print(X)

# a string and a number with the + operator, Python will give you an error
print(x + X)

# Make sure the number of variables matches the number of values, or else you will get an error.

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z)
print(x + y + z)

# Variables that are created outside of a function 

# x = "awesome"

def myfunc():
    global x          #keywprd to make variable global and vice-versa
    x = "fantastic"
    print("python is " + x)
    
myfunc()

print("python is " + x)
