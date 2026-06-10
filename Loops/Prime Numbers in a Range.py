start = int(input("Enter Start: "))
end = int(input("Enter End: "))

for num in range(start, end + 1):

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)