numbers = [1, 2, 3, 5, 6]

n = 6

total = n * (n + 1) // 2

sum_list = 0

for num in numbers:
    sum_list += num

missing = total - sum_list

print("Missing number:", missing)
