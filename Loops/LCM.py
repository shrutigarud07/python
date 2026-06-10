a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

largest = max(a, b)

while True:
    if largest % a == 0 and largest % b == 0:
        print("LCM =", largest)
        break

    largest += 1