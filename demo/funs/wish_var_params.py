def wish(*names, message="Hi"):
    for n in names:
       print(message, n)


wish("Larry", "Scott")
wish("Mark", "Jack", message="Hello")
