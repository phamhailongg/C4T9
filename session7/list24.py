from random import shuffle
w = input("Enter a word: ")
print("Jumbled word: ")
l = list(str(w))
shuffle(l)
for letters in l :
    print(letters)