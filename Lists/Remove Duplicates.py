numbers = [10, 20, 10, 30, 20, 40]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List after removing duplicates:", result)
