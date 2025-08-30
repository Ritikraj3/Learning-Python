thislist = ["apple", "banana", "cherry"]
thislist.append("orange")          #add item at end
print(thislist)

# insert items ---> insert anywhere in the list by giving index
thislist.insert(1,"watermelon")
print(thislist)

# Extend List
#--> To append elements from another list to the current list, use the extend() method
# The elements will be added to the end of the list.
fruits = ["strawberry", "kiwi", "mango"]
thislist.extend(fruits)
print(thislist)

# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)