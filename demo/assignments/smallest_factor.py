# Print smallest factor other than 1
num = 125

for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i)
        break
else:
    print(num)


