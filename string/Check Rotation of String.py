string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if len(string1) == len(string2) and string2 in (string1 + string1):
    print("Rotation of string")
else:
    print("Not Rotation")
