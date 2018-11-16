# game intro
from random import randint 
boss_life = 100 
your_life = 10
c = {
    "Name" : "Light" , 
    "Age" : 17 ,
    "Strength" : 8 ,
    "Defense" : 10 , 
    "HP" : 100 , 
    "Backpack" : ["Shield", "Bread loaf"] ,
    "Gold" : 100 ,
    "Level" : 2 
}

c["Gold"] += 50 
c["Backpack"].append("FlintStone")
c["Pocket"] = ["MonsterDex", "Flashlight"]
# print(c)
# skills
s = [
    {"Name" : "Tackle" ,
    "Minimum level" : 1 ,
    "Damage" : 5 ,
    "Hit rate" : 0.3 
    } ,

    {"Name" : "Quick attack" ,
    "Minimum level" : 2 ,
    "Damage" : 3 ,
    "Hit rate" : 0.5 
    } ,

    {"Name" : "Strong kick" , 
    "Minimum level" : 4 ,
    "Damage" : 7 ,
    "Hit rate" : 0.2
    }
]
# print(s)
for i in range(len(s)) : 
    print("Skill", i + 1)
    for key in s[i] : 
        print(key, ":", s[i][key])
print('_______________________')
print('')
print("Boss is coming ! Let's fight !")
# combat
while True : 
    
    b = input("Choose skill: ")
    while int(b) not in [1, 2, 3] : 
        b = input("Wrong key! Try again: ")
    b = int(b)
    if b > c["Level"] : 
        print("You have not learnt this skill yet! ")
    else : 
        ph = randint(0, 10) / 10
        if ph >= s[b]["Hit rate"] : 
            print("Damage:", s[b]["Damage"])
            boss_life -= s[b]["Damage"]
            print("Boss life remaining:", boss_life)
        else : 
            print("You missed !")
            your_life -= 0.5 
            print("Your blood:", your_life)
    if boss_life <= 0 : 
        print("Victory! You killed the boss")
        break
    else : 
        if your_life <= 0 : 
            print("You have been defeated! Game over!")
            break
        else : 
            print("Keep fighting !")
   
        
         
    
   