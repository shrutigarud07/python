numbers = [10, 20, 10, 30, 20, 10]

frequency = []

for num in numbers:
    if num not in frequency:
        frequency.append(num)
        print(num, ":", numbers.count(num))
