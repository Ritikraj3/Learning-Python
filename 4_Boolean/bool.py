print(10 > 9)
print(10 == 9)
print(10 < 9)

# message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# ====False Result=====

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False,
#  and that is if you have an object that is made from a class with a __len__ function that 
# returns 0 or False:
print("Some Values are False")
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# ---------------------

def myFunction() :
  return True

print(myFunction())

# ------------------------

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")