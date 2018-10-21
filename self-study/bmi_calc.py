name = "Long"
h = float(input("Your height ?"))
w = float(input("Your weight ?"))
bmi = w / ( h ** 2)
print("bmi: ")
print(bmi)
if bmi < 25: 
    print(name)
    print("is not overweight")
else :
    print(name)
    print("is overweight")
