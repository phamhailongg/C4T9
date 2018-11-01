#Ng dùng chơi quizz và có thể tự đặt câu hỏi
from random import randint
import random
#int check:
def not_int (a):
    try:
        int (a)
        return False 
    except ValueError:
        return True

set1 = [
    {"question": "Một cộng một bằng mấy?",
    "answer": "Hai",
    "wrong answer": ["Ba","Không đủ dữ liệu","Tất cả các đáp án"]
    },
    {"question":"Hai thêm hai bằng mấy?",
    'answer':"Bốn",
    'wrong answer': ["Hai","Không đủ dữ liệu", "Tất cả các đáp án"]
    }
]
set2 = [
    {"question": "2^10=?",
    "answer":"1024",
    "wrong answer": ["20","10^2","tất cả đáp án"]

    },
    {"question": "(0!+ 0! + 0!)!=?",
    "answer":"6",
    "wrong answer": ["0","3","Không ra gì"]
    }
]
set3 = [
    {"question": "Obama là tổng thống thứ mấy của Hoa Kỳ?",
    "answer":"44",
    "wrong answer": ["45","43","40"]

    },
    {"question": "Dân tộc Hoa (Việt Nam) có dân số gần nhất với?",
    "answer":"900,000",
    "wrong answer": ["1,000,000"," 90,000","100,000"]
    }
]
max_len = 0
level_switch = 0
question_set = [set1,set2,set3]
level = 0
picked =[]
scores = []
CHOICE = input('''Chọn chế độ:
[1]: Chơi
[2]: Tạo câu hỏi
''')
while CHOICE not in  ['1','2']:
    CHOICE = input ("Chỉ chọn 1 hoặc 2: ")
while CHOICE in ['1','2']: 
    if CHOICE == '1':
        print ('[CHƠI]')
        played = 0
        point = 0
        used = []
        level = input ("Chọn độ khó(dễ[1], trung bình[2], khó[3] ): ")
        while not_int(level) or (level not in ['1','2','3']):
            level= input("Chỉ nhập số(1, 2, hoặc 3):  ")
        level = int (level) 
        

        if level == 1:
            max_len = len(set1)+ len(set2)+len (set3)
        elif level == 2:
            max_len = len(set2)+len (set3)
        else :
            max_len = len(set3)

        while played < max_len:
            picked = question_set[level-1]
            pick_ques = randint(0,len(picked)-1)
            while pick_ques in used :
                pick_ques = randint(0,len(picked)-1)
            used.append (pick_ques)
            print (picked[pick_ques]['question'])
            display =  [ picked[pick_ques]['answer'] ]   +   picked[pick_ques]['wrong answer']
            display = random.sample (display, len(display))
            for i  in range (4):
                print (i+1,". ",display[i])
            response= (input ("Chọn đáp án của bạn:"))
            while not_int(response) or (response not in  ['1','2','3','4']):
                response = input ("Chỉ nhập số(1,2,3, hoặc 4)")
            response = int(response)
            played +=1
            level_switch +=1
            if display[response-1]== picked[pick_ques]['answer']:
                print ("ĐÚNG!")
                point += level
            else :
                print ("SAI!")
        
            if level_switch == len(picked):
                if level < 3 :
                    print ("Level up!")
                level +=1 
                level_switch = 0
                used = []
            print ("====================================")
        
        print ('FINAL SCORE:', point)
        if point not in scores:
            scores.append (point)
            scores  =  (sorted(scores, key=int, reverse=True))
        print ("High scores:")
    
        if len(scores) <= 4:
            for i in range (len(scores)):
                print (i+1,". ", scores[i], sep = '') 
        else :
            for i in range (5) :
                print (i+1,". ", scores[i], sep = '') 
        print ("##########################################")
        CHOICE = input ('''
        Chơi tiếp [1]
        Chuyển sang tạo câu hỏi [2]
        Thoát [phím khác]
        ''')


    else: 
        print ('[TẠO CÂU HỎI]')
        lvl =input ('Chọn độ khó: Dễ [1], Trung bình [2], Khó [3]:  ')
        while not_int (lvl) or (lvl not in ['1','2','3']):
            lvl = input ("Chỉ chọn 1,2,3:   ")
        lvl = int (lvl)
        restrict = []
        cau_hoi = input ("Nhập câu hỏi: ")
        dap_an_dung = input ("Nhập đáp án đúng:  ")
        restrict.append (dap_an_dung)
        dap_an_sai = []
        for i in range (0,3):
            print ("Nhập đáp án sai thứ ",i+1)
            s = input ()
            while (s in restrict):
                s = input("Đáp án trùng nhau, nhập lại:  ")
            restrict.append(s)
            dap_an_sai.append(s)
        new = {}
        new ['question'] = cau_hoi
        new ['answer'] = dap_an_dung
        new ['wrong answer']=dap_an_sai
        question_set[lvl-1].append(new)
        CHOICE = input('''
        Tiếp tục [2]
        Chuyển sang chơi [1]
        Thoát [phím khác]
        ''')