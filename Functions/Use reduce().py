from functools import reduce

numbers = [1, 2, 3, 4, 5]

def multiply(a, b):
    return a * b

result = reduce(multiply, numbers)

print("Product:", result)
