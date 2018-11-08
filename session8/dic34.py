# Who is the millionare ? 
from random import randint
import random
# int check:
def not_int (a):
    try:
        int (a)
        return False 
    except ValueError:
        return True

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

    {"Question" : "How many legs does an crab have" ,
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
    }
]
life = 3
max_len = 0
level_switch = 0
question_set = [s1, s2, s3]
level = 0
picked =[]
scores = []
CHOICE = input('''Do you want to play or check out the tutorial ?
[1]: Play
[2]: Solution
''')
while CHOICE not in  ['1','2']:
    CHOICE = input ("Choose 1 or 2: ")
while CHOICE in ['1','2']: 
    if CHOICE == '1':
        print ('[PLAY]')
        played = 0
        point = 0
        used = []
        level = input ("Chọn độ khó (Easy [1], Normal [2], Hard [3] ) : ")
        while not_int(level) or (level not in ['1','2','3']):
            level= input("Only digit (1, 2, hoặc 3): ")
        level = int (level) 
        

        if level == 1:
            max_len = len(s1) + len(s2) + len (s3)
        elif level == 2:
            max_len = len(s2) + len(s3)
        else :
            max_len = len(s3)

        while played < max_len:
            picked = question_set[level-1]
            pick_ques = randint(0, len(picked)-1)
            while pick_ques in used :
                pick_ques = randint(0, len(picked)-1)
            used.append (pick_ques)
            print (picked[pick_ques]["Question"])
            display =  [ picked[pick_ques]["Answer"] ]   +   picked[pick_ques]["Wrong answers"]
            display = random.sample(display, len(display))
            for i  in range (4):
                print (i + 1, ".", display[i])
            response= (input("Your answer: "))
            while not_int(response) or (response not in  ['1', '2', '3', '4']) :
                response = input ("Only these answer (1,2,3, or 4)")
            response = int(response)
            played +=1
            level_switch +=1
            if display[response-1] == picked[pick_ques]["Answer"] :
                print ("ĐÚNG!")
                point += level
            
            else :
                print ("SAI!")
                life -= 1
                print("Life remaining: ", life)
        
            if level_switch == len(picked) :
                if level > 3 :
                    print ("Level up!")
                level += 1 
                level_switch = 0
                used = []
            print ("_______________________________")
            
        print ('FINAL SCORE:', point)
        if point not in scores:
            scores.append(point)
            scores  =  (sorted(scores, key = int, reverse = True))
        print ("High scores:")
    
        if len(scores) <= 4:
            for i in range (len(scores)):
                print (i+1, ". ", scores[i], sep = '') 
        else :
            for i in range (5) :
                print (i+1,". ", scores[i], sep = '') 
        print ("                    *  *  *                     ")
        CHOICE = input ('''
        Keep playing [1]
        Check solution [2]
        Quit [Other key]
        ''')
    else : 
        print ("Đoán xem! Cuộc sống mà")
        break