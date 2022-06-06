data = ["1000,87,e,87,76", "1003,76,a,99,99,98,65", "1008,76,55,39"]


def sort_by_avg(tup):
    # print(tup)
    marks = tup[1]
    return sum(marks) / len(marks)


students = {}
for entry in data:
    entries = entry.split(",")
    admno = entries[0]
    valid_entries = filter(str.isdigit, entries[1:])
    marks = list(map(int, valid_entries))
    students[admno] = marks

for admno, marks in sorted(students.items(), key=sort_by_avg):
    total = sum(marks)
    avg = total / len(marks)
    print(f"{admno:5} {total:4} {avg:5.2f}")
