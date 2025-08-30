thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
 
print(thislist[:3])
print(thislist[1:3])
print(thislist[-4:-1])   # -1 excluding last element
print(thislist[1:])

# Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the list")