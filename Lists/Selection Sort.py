numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    smallest = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[smallest]:
            smallest = j

    numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

print("Sorted list:", numbers)
