data = ["87,e,87,76", "76,a,55,98,65", "76,55,39"]

for entry in data:
    valid_entries = filter(str.isdigit, entry.split(","))
    marks = list(map(int, valid_entries))
    print(f"{sum(marks):4} {sum(marks) / len(marks):5.2f}")