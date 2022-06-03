# Keyword-only args
def wish(*, name, message="Hi"):
    print(f"{message} {name}")


# wish("Tom")
# Keyword args
wish(message="Hi", name="Scott")
wish(name="Steve", message="Good Morning")
