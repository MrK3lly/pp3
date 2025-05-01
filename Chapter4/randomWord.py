""" computer to pick a word
display how many letters in word
player gets 5 chances
computer responds with only yes or no """

import random

selection = ['apple', 'banana', 'cherry', 'date', 'elderberry', "Stack", "Overflow", "rocks", "Python", "is", "awesome"]

word = random.choice(selection)

letter = len(word)

print("The word has", letter, "letters")

chances = 5

while chances:
    guess = input("Please guess the word I am thinking of: ")
    if guess == word:
        print("You guessed it!")
        break
    else:
        chances -= 1
        for letter in guess:
            if letter in word:
                print("Yes, the letter", letter, "is in the word.")
            else:
                print("No, the letter", letter, "is not in the word.")
        print("You have ", chances, " left.")


""" while chances:
    guess = input("Please guess the word I am thinking of: ")
    if guess == word:
        print("You guessed it!")
    else:
        print("Wrong guess, try again.")
        chances -= 1  """   
