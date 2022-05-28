# Print given names in sorted order
names = []

while True:
    name = input("Enter name [end to stop]: ")
    if name == 'end':
        break

    names.append(name)

for name in sorted(names):
    print(name)

