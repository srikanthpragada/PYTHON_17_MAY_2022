# Print largest factor other than the number
num = 19

for i in range(num//2, 0, -1):
    if num % i == 0:
        print(i)
        break


