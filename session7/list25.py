# game 
from random import shuffle
from random import randint
life = 3
l = ['spider Man', 'photography', 'music', 'dragon ball', 'sport', 'porn', 'one punch man']
def scramble(words) : 
    words = list(words)
    shuffle(words)
    return "".join(words)
while life > 0 : 
    print("Life remains: ", life)
    og = l[randint(0, len(l) - 1)]
    nw = scramble(og)
    print("Scramble word: ", nw)
    r = input("Your answer: ")
    if r == og : 
        print("True!")
    else : 
        print("False!")
        life -= 1
print("Nghỉ mẹ game đi!")