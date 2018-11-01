p = input("Your password? ")
while True :
    if p.isalpha() or p.isdigit() : 
        p = input("Password must have at least 8 characters, Type again ")
    else : 
        if len(p) < 8 : 
            p = input("Password must have at least 8 characters ")
        else : 
            print("Welcome")
            break