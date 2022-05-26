total = 0
while True:
    num = int(input("Enter number :"))
    if num == 0:
        break

    if num < 0:
        continue

    total += num  # total = total + num

print('Total   =', total)
