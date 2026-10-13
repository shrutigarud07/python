numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

groups = {}

for num, count in frequency.items():
    if count not in groups:
        groups[count] = []
    groups[count].append(num)

print(groups)
