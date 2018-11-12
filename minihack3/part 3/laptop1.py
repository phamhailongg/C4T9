# menu
p = {
    "HP" : 600 ,
    "DELL" : 650 , 
    "MACBOOK" : 12000 , 
    "ASUS" : 400 ,
    "ACER" : 350 , 
    "TOSHIBA" : 600 ,
    "FUJITSU" : 900 , 
    "ALIENWARE" : 1000
}

# ASUS price
print("The price of Asus is", p["ASUS"])

# Checked by users
c = input("Which laptop do you want to check? ")
while c not in p : 
    c = input("We can not found your laptop! Try anothers: ")
print("The price of", c, "is", p[c] )

# Bill
print("Number of ASUS:", 5)
print("The total bill is", p["ASUS"] * 5)

# Sellers & Buyers
b = input("Which brand of laptop you want to buy? ")
while b not in p : 
    b = input("We can not found your laptop! Try anothers: ")
n = int(input("Quantity: "))
print("The total bill is", p[b] * n)


