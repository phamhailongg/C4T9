# C R U D
l = ['Spider Man', 'Photography', 'Music']
print("Current list: ", l)

while True :
    choice = input("C to create new things, R to read elements, U to update new things, D to delete things. I will choose: ")
    while choice not in ['c','r','u','d']:
        choice = input("Invalid choice! Retry: ")
    if choice == "c" : 
        n1 = input("Which one do you wanna add? ")
        l.append(n1)
        print("You now get a new list: ", l)
    elif choice == "r" :
        for n, things in enumerate(l) : 
             print(n + 1, ". ", things, sep="")      
    elif choice == "u" :
        p1 = int(input("Which position you wanna change? "))
        while p1 > len(l) - 1 : 
            p1 = int(input("Invalid position! Try again! ")) 
        n2 = input("New thing you gonna change: ")
        l[p1] = n2 
        print("You will get a new list: ", l)
    else : 
        p2 = int(input("Which position you wanna delete? "))
        while p2 > len(l) - 1 : 
            p2 = int(input("Invalid position! Try again! "))
        l.pop(p2)
        print("You will get a new list: ", l)


        
