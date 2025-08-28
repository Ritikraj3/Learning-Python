
age = 36
#This will produce an error:
# txt = "My name is John, I am " + age

# F-String --- 
# --To specify a string as an f-string, simply put an f in front of the string literal, 
# and add curly brackets {} as placeholders for variables and other operations.

txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers---
# A modifier is included by adding a colon : followed by a legal formatting type, 
# like .2f which means fixed point number with 2 decimals

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {price * 2} dollars"
print(txt)