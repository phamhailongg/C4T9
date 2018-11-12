# laptop
l = {
    "HP" : 20 ,
    "DELL" : 50 ,
    "MACBOOK" : 12 ,
    "ASUS" : 30
}

# print each row
for k, v in l.items() :  
    print(k, ":", v)

# number of laptops  
print("We are counting! Please wait...")
print("The number of laptops is" , sum(l.values()))

# add more brands of laptop
l["FUJITSU"] = 15 
l["ALIENWARE"] = 5 

# sum 
print("We are counting! Please wait...")
print("The number of laptops is" , sum(l.values()))
