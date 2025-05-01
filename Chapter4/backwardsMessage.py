# prints message backwords

word = input(" Please give my a word, ")

print("You word has this many characters" , len (word))

letters = len(word)

print(word[::-1])

start = len(word)
end = -len(word)

print(start)
print(end)

i = len(word)

while i > 0:
    i -= 1
    print(word[i])