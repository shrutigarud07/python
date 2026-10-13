student = {
    "name": "Shruti",
    "city": "Pune",
    "course": "Computer"
}

inverted = {}

for key, value in student.items():
    inverted[value] = key

print(inverted)
