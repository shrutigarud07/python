string = input("Enter a string: ")

seen = ""

for ch in string:
    if ch in seen:
        print("First repeated character:", ch)
        break
    seen += ch
