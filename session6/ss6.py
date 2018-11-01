print("How many legs does a spider have? ")
print("1. None")
print("2. 4 legs")
print("3. 8 legs")
print("4. 12 legs")

a = input("Your answer: ")
while True :
    if a.isalpha() :
        a = input("The answer must be 1, 2, 3 or 4, enter again: ")
    else:
        if int(a) != 3 :
            print("Wrong, the answer is 3: 4 legs")
            break
        else:
            print("Correct")
            break
