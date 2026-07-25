string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not Anagram")
