message = input("Please enter a word: ")

new_message = ""

VOWELS = "aeiou"

for letter in message:
    if letter not in VOWELS:
        new_message += letter
        print("A new string has been created: ", new_message)