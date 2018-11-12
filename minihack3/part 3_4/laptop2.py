# export processing...
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

q = {
    "HP" : 20 ,
    "DELL" : 60 ,
    "MACBOOK" : 2 ,
    "ASUS" : 30 ,
    "ACER" : 20 ,
    "TOSHIBA" : 10 ,
    "FUJITSU" : 15 ,
    "ALIENWARE" : 5
}
l = []
for key in p : 
    l.append(key)

# check laptop
def check(x) : 
    x = x.upper()
    r1 = 0
    r2 = 0
    r3 = 0
    lx = x.split(":")
    if len(lx) < 2 : 
        r1 = 1 
        print("Missing ':' ! Please try again : ")
    else : 
        if int(lx[1]) <= 0 : 
            r2 = 1 
            print("Wrong quantity !")
        if lx[0] not in l : 
            r3 = 1 
            print("This brand does not exist in our store !")
    fr = r1 + r2 + r3
    return (fr != 0)

# total 
total = 0 
for key in p : 
    price = p[key] * q[key]
    total += price
    print("Total price of", key, ":", price)
print("Total price of all the laptops is", total)

# export laptop from company 
e = input("Choose your brand and quantity ( Seperated by ':' ): ")
while check(e) : 
    e = input("Choose your brand and quantity ( Seperated by ':' ): ")
o = e.split(':')
b = o[0].upper()
q = int(o[1])
prize = p[b] * q 
print("Total bill:", prize)



