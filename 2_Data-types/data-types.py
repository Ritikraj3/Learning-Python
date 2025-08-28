"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
# Getting the Data Type
x = int(5.2)
print(x)

x=2e1
print(type(x))

x = 3j
print(type(x))

import random
print(random.randrange(1,10))
print("It's 'alright'")


import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("shut up!")
engine.runAndWait()