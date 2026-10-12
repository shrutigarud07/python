marks = {
    "Rahul": 75,
    "Amit": 90,
    "Sneha": 65,
    "Priya": 85
}

sorted_dict = dict(sorted(marks.items(), key=lambda item: item[1]))

print(sorted_dict)
