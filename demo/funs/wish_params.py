def wish(name: str, message: str):
    print(f"{message} {name}")


# Positional args
wish("Larry", "Hi")
wish("James", "Hello")

# Keyword args
wish(message="Hi", name="Scott")
wish("Steve", message="Good Morning")
