# 🧮 Python Operators — Complete & Well-Structured Guide with Examples

A practical README-style reference to Python **operators** — explained clearly, grouped by category, and illustrated with runnable examples. Copy the examples into a Python REPL or script to try them out.

---

## 🔎 Overview

Python operators are symbols or keywords that perform operations on values and variables.
Main categories covered here:

* Arithmetic
* Assignment (including walrus `:=`) & Augmented Assignment
* Comparison
* Logical
* Bitwise
* Membership
* Identity
* Conditional (ternary)
* Operator precedence, tips & gotchas

---

## ➕ Arithmetic Operators

Used for numeric calculations.

```python
a = 7
b = 3

print(a + b)   # 10
print(a - b)   # 4
print(a * b)   # 21
print(a / b)   # 2.3333333333333335  (float division)
print(a // b)  # 2                   (floor division)
print(a % b)   # 1                   (remainder)
print(a ** b)  # 343                 (7 to the power 3)

# Unary
print(-a)      # -7
print(+b)      # 3
```

**Notes**

* `/` always gives float (Python 3).
* `//` is floor division (useful for integers or to drop fractional part).
* `**` is exponentiation.

---

## 📝 Assignment Operators & Walrus (`:=`)

Simple assignment and the walrus operator (assignment expression introduced in Python 3.8).

```python
x = 5
y = x + 2
print(x, y)  # 5 7

# Walrus operator: assign inside an expression
if (n := len([1, 2, 3])) > 2:
    print("Length is", n)  # Length is 3
```

**When to use walrus**: when you want to both compute and reuse a value inside an expression (e.g., loops, conditionals).

---

## 🔁 Augmented Assignment

Shorter in-place updates: `+=`, `-=`, `*=`, etc.

```python
x = 10
x += 5    # same as x = x + 5
print(x)  # 15

# Caution with mutable types
lst = [1, 2]
lst += [3]   # modifies list in place -> [1, 2, 3]
print(lst)
```

---

## ✅ Comparison Operators

Compare values — return `True` or `False`.

```python
print(5 == 5)    # True
print(5 != 3)    # True
print(3 < 5)     # True
print(5 >= 5)    # True

# Chained comparisons
print(1 < 2 < 3) # True
```

**Tip**: Comparisons are chainable (and are evaluated efficiently / short-circuit).

---

## 🔐 Logical Operators

`and`, `or`, `not` — operate on boolean values, but return actual operands (truthy/falsy values).

```python
print(True and False)    # False
print(True or False)     # True
print(not True)          # False

# Short-circuiting / truthiness:
print(0 and 5)           # 0  -> 0 is falsy, returned immediately
print(1 and 5)           # 5  -> first truthy, returns second value
print("" or "hello")     # "hello" -> empty string falsy, returns "hello"
```

**Behavior**: `and` returns the first falsy value or last value; `or` returns the first truthy value or last value.

---

## 🔢 Bitwise Operators

Operate on the binary representations of integers: `&`, `|`, `^`, `~`, `<<`, `>>`.

```python
x = 5   # binary 0101
y = 3   # binary 0011

print(x & y)   # 1   (0101 & 0011 == 0001)
print(x | y)   # 7   (0101 | 0011 == 0111)
print(x ^ y)   # 6   (0101 ^ 0011 == 0110)

print(~x)      # -6  (bitwise NOT; in Python ~x == -x - 1)

print(1 << 3)  # 8   (left shift: 0001 -> 1000)
print(8 >> 2)  # 2   (right shift)
```

**Note about `~`**: Python uses infinite-precision signed integers; `~x` equals `-x - 1`.

---

## 🔎 Membership Operators

`in`, `not in` — check whether value is contained in a sequence or collection.

```python
print('a' in 'cat')         # True
print(2 in [1, 2, 3])       # True
print('x' not in 'hello')   # True
```

Works with strings, lists, tuples, sets, dict keys, etc.

---

## 🧩 Identity Operators

`is`, `is not` — test whether two references point to the **same object**.

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)   # True   (same object)
print(a is c)   # False  (different objects, same contents)
print(a == c)   # True   (contents equal)

x = None
print(x is None)  # recommended way to check for None
```

**Important**: use `==` to compare values, use `is` for identity (same object).

---

## ❓ Conditional (Ternary) Operator

Inline if-else expression: `A if condition else B`.

```python
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"
```

Useful for concise expressions; avoid over-nesting to keep readability.

---

## 📐 Operator Precedence (Simplified)

Higher precedence operators are evaluated first. Use parentheses `()` to make intent explicit.

From **higher** to **lower** (common subset — see official docs for the full table):

1. `()` (parentheses, grouping)
2. `**` (exponentiation)
3. unary `+`, `-`, `~` (note: exponentiation binds tighter than unary minus: `-2**2 == -(2**2)`)
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. Comparisons: `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`
11. `not`
12. `and`
13. `or`
14. conditional expression `x if C else y` and assignment constructs are lower-level than most operators (and `lambda` is one of the lowest)

**Rule of thumb:** If an expression might be ambiguous, add parentheses — it's clearer and safer.

---

## ⚠️ Common Gotchas & Best Practices

* `==` vs `is`: use `==` for equality, `is` to check identity (e.g., `is None`).
* Integer division: `/` gives float, `//` floors result.
* Exponent vs unary minus: `-2**2` equals `-4`. Use `(-2)**2` for `4`.
* Floating point precision: rounding issues (`0.1 + 0.2 != 0.3` exactly). For money, use `decimal`.
* For string concatenation of many pieces, prefer `str.join()` over repeated `+` for performance.
* Bitwise `~` behaves as `-x - 1` — surprising if you expect bit-limited integers.
* Augmented assignment (`+=`) can mutate a mutable object in-place; be cautious when sharing references.

---

## 🔁 Quick Reference Examples (Ready to Paste)

```python
# Arithmetic
print((7 // 3, 7 / 3, 7 % 3))   # (2, 2.3333333333333335, 1)

# Comparisons
print(1 < 2 < 3)                 # True

# Logical short-circuit
print("" or "fallback")          # "fallback"
print([] and "nope")             # []

# Bitwise
print(bin(5), bin(3), 5 & 3)     # '0b101' '0b11' 1

# Membership
print('p' in 'python')           # True

# Identity
a = [1]; b = a; c = [1]
print(a is b, a is c, a == c)    # True False True

# Ternary
print("yes" if True else "no")   # "yes"
```

---

## ✨ Final Notes

* Operators are fundamental — practice by writing small snippets and predicting results.
* Use parentheses generously while learning precedence — they make code easier to read.
* When unsure about a behavior (e.g., `~`, `//`, `is`), test small examples in REPL.
