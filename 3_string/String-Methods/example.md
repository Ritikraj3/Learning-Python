
# 🐍 Python String Methods Cheat Sheet

A handy list of Python string methods with **simple explanations + examples**.

---

## 🔤 String Modification

```python
txt = "hello world"

print(txt.capitalize())   # "Hello world"
print(txt.casefold())     # "hello world"
print(txt.center(20))     # "    hello world     "
print("hi\tpython".expandtabs(10))  # "hi        python"
print(txt.lower())        # "hello world"
print("   hello ".lstrip())   # "hello "
print("   hello ".rstrip())   # "   hello"
print("   hello ".strip())    # "hello"
print("HeLLo".swapcase())     # "hEllO"
print("welcome to python".title())   # "Welcome To Python"
print(txt.upper())        # "HELLO WORLD"
print("42".zfill(5))      # "00042"
```

---

## 🔍 Searching & Finding

```python
txt = "hello world hello"

print(txt.count("hello"))     # 2
print(txt.find("world"))      # 6
print(txt.rfind("hello"))     # 12
print(txt.index("world"))     # 6
print(txt.rindex("hello"))    # 12
print(txt.startswith("he"))   # True
print(txt.endswith("lo"))     # True
```

---

## 🧩 String Tests (Return `True`/`False`)

```python
print("abc123".isalnum())     # True
print("abc".isalpha())        # True
print("hello".isascii())      # True
print("1234".isdecimal())     # True
print("1234".isdigit())       # True
print("½".isnumeric())        # True
print("name".isidentifier())  # True
print("hello".islower())      # True
print("HELLO".isupper())      # True
print("Hello!".isprintable()) # True
print("   ".isspace())        # True
print("Hello World".istitle())# True
```

---

## 🛠️ String Operations

```python
txt = "hello"

# Encoding
print(txt.encode())   # b'hello'

# Formatting
print("My name is {}".format("Ritik"))      # "My name is Ritik"
print("Coordinates: {x}, {y}".format_map({"x": 10, "y": 20}))  
# "Coordinates: 10, 20"

# Joining
print(",".join(["a", "b", "c"]))    # "a,b,c"

# Justify
print(txt.ljust(10, "-"))   # "hello-----"
print(txt.rjust(10, "-"))   # "-----hello"

# Translation
table = str.maketrans("h", "H")
print(txt.translate(table)) # "Hello"

# Partition
print("python=fun".partition("="))   # ('python', '=', 'fun')
print("python=fun".rpartition("=")) # ('python', '=', 'fun')

# Replace
print("hello world".replace("world", "Python"))  # "hello Python"

# Split
print("a,b,c".split(","))   # ['a', 'b', 'c']
print("a,b,c".rsplit(",", 1)) # ['a,b', 'c']
print("hello\nworld".splitlines()) # ['hello', 'world']
```

---
