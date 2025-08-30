thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1] = "strawberry"
print(thislist)

# Change a Range of Item Values

thislist[0:3] = ["raspberry", "watermelon"]     #--> 1st value is 'index' and 2nd value is 'range'
print(thislist)


# Insert Items ---> insert() method 
# insert a new list item, without replacing
thislist.insert(0, "chocolate")     #this will increase the length of the list
print(thislist)
