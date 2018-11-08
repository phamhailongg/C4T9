# Who will be the millianare ? 
from random import randint
import random

# Create quiz ! 
s1 = [
    {"Question" : "How many legs does an octopus have ?" ,
    "Answer" : "Eight legs" ,
    "Wrong answers" : ["One leg", "Two legs", "Four legs"] ,
    } ,
    
    {"Question" : "Why is the letter E so important ?" ,
    "Answer" : "Because it is the beginning of everything" ,
    "Wrong answers" : ["Who knows ?", "Who care ?", "I do not know !"] ,
    } ,

    {"Question" : "How many legs does an crab have ?" ,
    "Answer" : "Eight legs" ,
    "Wrong answers" : ["Zero leg", "It swims", "Four legs"] ,
    }
]
s2 = [
    {"Question" : "What has nothing but a head and a tail ?" ,
    "Answer" : "A coin" ,
    "Wrong answers" : ["An animal", "Human", "A bee"] ,
    } ,

    {"Question" : "Who works only one day in a year but never gets fired ?" , 
    "Answer" : "Santa Claus" ,
    "Wrong answers" : ["Me", "Myself", "I"] ,
    } ,

    {"Question" : "What has arms but can not hug ?" ,
    "Answer" : "Armchair" ,
    "Wrong answers" : ["Heart", "You", "Your Crush"] ,
    } ,

    {"Question" : "Which run is live, not run is dead ?" ,
    "Answer" : "A Heart" ,
    "Wrong answers" : ["Human", "A Clock", "None of them"] ,
    } 
]
s3 = [
    {"Question" : "Why are dogs afraid to sunbathe ?" ,
    "Answer" : "Becoming Hot-Dog" ,
    "Wrong answers" : ["I do not know", "Bee", "Ridiculous"] ,
    } ,

    {"Question" : "What clothing is always sad ?" ,
    "Answer" : "Blue jeans" ,
    "Wrong answers" : ["Hoodie", "Tank-top", "T-Shirt"] ,
    } ,

    {"Question" : "Why does the bee always work ?" ,
    "Answer" : "Because it is Bee-sy" ,
    "Wrong answers" : ["Do not care much", "Who knows", "Weird"] ,
    } ,

    {"Question" : "Which one lying is standing and reversed ?" ,
    "Answer" : "A foot" ,
    "Wrong answers" : ["A Road", "A sword", "None of them"] ,
    } ,

    {"Question" : "Who is the king of the jungle ?" ,
    "Answer" : "A tiger" ,
    "Wrong answers" : ["A lion", "A leopard", "Annaconda"] ,
    }
]

life = 3 
nqiz = 0
ls = 0
QS = [s1, s2, s3]
level = 0 
Qpiked = []
scores = []
c = input('''
[1] : Play
[2] : Solution
''')
while c not in ["1", "2"] : 
    c = input("Invalid key! Choose again! ")
while c in ["1", "2"] : 
    if c == "1" :
        print("[Let's Play]")
        turns = 0
        point = 0
        Qused = []
        level = input('''Choose level : 
        [1] : Easy
        [2] : Normal
        [3] : Hard
        ''')
        while level not in ["1", "2", "3"] : 
            level = input("Invalid key! Choose again! ")
        level = int(level)
        

        if level == 1 : 
            n0qiz = len(s1) + len(s2) + len(s3)
        elif level == 2 : 
            n0qiz = len(s2) + len(s3)
        else : 
            n0qiz = len(s3)
        
        while turns < n0qiz : 
            # Edit questions
            Qpiked = QS[level - 1]
            Pquiz =  randint(0, len(Qpiked) - 1)
            while Pquiz in Qused : 
                Pquiz = randint(0, len(Qpiked) - 1)
            Qused.append(Pquiz)
            print(Qpiked[Pquiz]["Question"])
            # Edit answers :
            diz = [ Qpiked[Pquiz]["Answer"] ] + Qpiked[Pquiz]["Wrong answers"]    
            diz = random.sample(diz, len(diz))
            for i in range(4) : 
                print(i + 1, ".", diz[i])
            a = input("Your answer: ")
            while a not in ["1", "2", "3", "4"] : 
                a = input("Invalid answers! You can only choose one from 1 to 4! Again : ")
            a = int(a)
            turns += 1
            ls += 1 
            if diz[a - 1] == Qpiked[Pquiz]["Answer"] : 
                print("True !")
                point += 1
                print("Life remaining: ", life)
            else : 
                print("Wrong !")
                print("The true answer must be: ", Qpiked[Pquiz]["Answer"])
                life -= 1
                print("Life remaining: ", life)
                if life == 0 : 
                    print("Game over !")
                    break
            
            
            if ls == len(Qpiked) : 
                if level < 3 : 
                    print("You did try so hard ! Keep it up")
                level += 1
                ls = 0
                Qused = []  
        print("Final score: ", point)
        if point not in scores : 
            scores.append(point)
            scores = sorted(scores, key = int, reverse = True)
        print("High score: ")

        if len(scores) <= 4 :  
            for i in range(len(scores)) : 
                print(i + 1, ".", scores[i], sep="")
        else : 
            for i in range(5) : 
                print(i + 1, ". ", scores[i], sep ="")   
        print('''
                                *   *   *
        ''')
        c = input('''
        [1] : Keep playing
        [2] : Check solution
        [Other key] : Quit
        ''')
    else : 
        print("Đoán xem! Cuộc sống mà :) ! Bye ! ")
        break