scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
grades = {}

for i in scores:
    if scores[i] > 90:
        grades[i] = "Outstanding"
    elif scores[i]> 80:
        grades[i] = "Exceeds Expectations"
    elif scores[i]> 70:
        grades[i] = "Acceptable"
    else:
        grades[i] = "Fail"

print(grades)
