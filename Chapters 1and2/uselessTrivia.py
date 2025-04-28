# Useless Trivia
#
# Gets personal information from the user and then
# prints true but useless information about the user.

name = input("What is your name? ")

age = int(input("How old are you? "))

weight = int(input("How many kilos do you weigh?"))

print("\nIf poet ee cumings were to email you, he'd address you as ", name.lower())

print("but if ee were mad, he'd call you ", name.upper())

called = name * 5

print("\nIf a small child were to call you, he would say ", called)

seconds = age *365 * 24 * 60 * 60

print("\nYou are over ", seconds, "seconds old.")
      
moon_weight = weight / 6

print("\nIf you were on the moon, you would weigh ", moon_weight, "kilos.")

input("\n\nPress the enter key to exit.")
