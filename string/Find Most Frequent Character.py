string = input("Enter a string: ")

max_count = 0
most = ""

for ch in string:
    if string.count(ch) > max_count:
        max_count = string.count(ch)
        most = ch

print("Most frequent character:", most)
