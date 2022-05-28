# Validate password - One Upper, One Digit and One Special char - _ # @
pwd = "Abc_123"

upper = digit = special = False
for c in pwd:
    if c.isupper():
        upper = True
    elif c.isdigit():
        digit = True
    elif c in '#_@':
        special = True

if upper and digit and special:
    print("Valid")
else:
    print("Invalid")
