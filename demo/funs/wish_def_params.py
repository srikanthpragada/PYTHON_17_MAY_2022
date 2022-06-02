# Default param
def wish(name="Guest", message="Hello"):
    print(f"{message} {name}")


# Positional args
wish("Larry", "Hi")
wish("James")
wish()

# Keyword args
wish(message="Hi", name="Scott")
wish(name="Tom")
wish("Steve", message="Good Morning")
wish(message="Hi")
