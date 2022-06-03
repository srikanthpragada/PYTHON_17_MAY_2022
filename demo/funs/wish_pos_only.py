# Keyword-only args
def wish(name, msg="Hi", /):
    print(f"{msg} {name}")


wish("Tom", "Hello")
# Positional only args
wish("Steve")
# wish(message="Hi", name="Scott")
