base = int(input("Enter Base: "))
power = int(input("Enter Power: "))

result = 1

for i in range(power):
    result *= base

print("Answer =", result)