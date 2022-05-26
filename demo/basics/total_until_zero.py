total = 0
for i in range(10):
    num = int(input("Enter number :"))
    if num == 0:
        break

    total += num  # total = total + num

print('Total   =', total)
