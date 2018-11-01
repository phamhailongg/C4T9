p = input("Your Pasword? ")
while True : 
    if p.isalpha() or p.isdigit() :
        p = input("Password must have both numbers and letters, Type again ")
    else : 
        if p.islower() or p.isupper() :
            p = input("Password must have at least 1 uppercase, Type again ")
        else :
            if len(p) < 8 : 
                p = input("Password must have at least 8 characters, Type again ")  
            else : 
                print("Welcome")
            break 