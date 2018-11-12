# laptop
l = {
    "HP" : 20 ,
    "DELL" : 50 ,
    "MACBOOK" : 12 ,
    "ASUS" : 30
}

# check n0 of mac
print("Number of Macbooks left:", l["MACBOOK"])

# check by users
m = input("Which laptop do you want to check? ")
while m not in l : 
    m = input("Invalid laptop ! Type again please: ")
print("Number of", m, "left:", l[m])

# add a new brand of laptop
l["TOSHIBA"] = 10
print(l)

# added by users
c = input("Your brand of laptop: ")
n = int(input("Number of laptops you want to add: "))
l[c] = n
print(l)

# add more laptops 
l["DELL"] +=10 
l["MACBOOK"] = 2
print(l)