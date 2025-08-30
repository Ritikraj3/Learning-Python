thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# If you do not specify the index, the pop() method removes the last item.
thislist.pop()
print(thislist)

# The 'del' keyword also removes the specified index:
del thislist[0]
print(thislist)

# The 'del' keyword can also delete the 'list' completely.
# del thislist
# print(thislist)

# Clear the List
thislist.clear()
print(thislist)