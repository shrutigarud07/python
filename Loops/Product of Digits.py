num = int(input("Enter Number: "))

product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10

print("Product =", product)