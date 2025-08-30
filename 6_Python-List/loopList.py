thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print("---------------")

# through index number
for i in range(len(thislist)):
    print(thislist[i])

print("---------------")

# Using a While Loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

print("---------------")

[print(x) for x in thislist]