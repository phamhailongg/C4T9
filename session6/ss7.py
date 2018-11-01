p = input("Your password? ")
while True :
    if p.isalpha() == True :
        p = input("Invalid Password! Type again! ")
    else :
        if p.isdigit() :
            print("Welcome")
            break