marks = []
while True:
    n = int(input("Enter marks [0 to stop] :"))
    if n == 0:
        break

    marks.append(n)

avg = sum(marks) // len(marks)

for n in marks:
    if n > avg:
        print(n)


