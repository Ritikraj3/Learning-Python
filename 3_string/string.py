# 'hello' is the same as "hello".

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

# in the result, the line breaks are inserted at the same position as in the code.
a = """
oifnrwif
oknioir
oirfew
coinewoinwevoinwvo
"""
print(a)

# Strings are Array
a = "Ritik Raj"
print(a[0])

# Looping through a String
for x in a:
    print(x)

# Length of String
print(len(a))

# Check in String
print("R" in a)

# check with (if)
if "Ritik" in a:
    print("yes")

# check if not
print("R" not in a)

# check if not with (if)
if "Hello" not in a:
    print("No, its not present in a")