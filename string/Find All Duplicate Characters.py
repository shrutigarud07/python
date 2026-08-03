string = input("Enter a string: ")

duplicate = ""

for ch in string:
    if string.count(ch) > 1 and ch not in duplicate:
        duplicate += ch

print("Duplicate characters:", duplicate)
