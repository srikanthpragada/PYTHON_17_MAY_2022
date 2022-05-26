
total = count = 0
for i in range(5):
    num = int(input("Enter number :"))
    if num > 0:
        total += num    # total = total + num
        count += 1

print('Total   =', total)
print('Average =', total // count)

