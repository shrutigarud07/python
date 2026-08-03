string = input("Enter a sentence: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for ch in alphabet:
    if ch not in string:
        print("Not a Pangram")
        break
else:
    print("Pangram")
