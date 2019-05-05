# def Find_Cranes_Num(total_legs, num_turtles):
#     return (total_legs - 4 * num_turtles) // 2
# while True :
#     total_legs_x = int(input("Input the total of legs: "))
#     num_turtles_y = int(input("Input the number of turtles: "))
#     num_cranes = Find_Cranes_Num(total_legs_x, num_turtles_y)
#     if total_legs_x < ( 4 * num_turtles_y ) : 
#         print("Number of Cranes must be larger than 0! Try again!")
#     else: 
#         print("Number of Cranes is :", num_cranes)

# def my_abs(x) :
#     if x >= 0 :
#         print(x)
#     else :
#         print(-x)
        
# my_abs(-11123)

# h = float(input("Your height: "))     # height(m)
# w = float(input("Your weight: "))     # weight(kg)
# a = int(input("Your age: "))
# bmi = w / ( h ** 2)

# if bmi < 22.0 and a < 45 : 
#     print("Your BMI is", round(bmi, 2),". Your risk of heart diseases is LOW!")
# elif bmi < 22.0 and a >= 45 :
#     print("Your BMI is", round(bmi, 2),". Your risk of heart diseases is MIDDLE!")
# elif bmi >= 22.0 and a < 45 : 
#     print("Your BMI is", round(bmi, 2),". Your risk of heart diseases is MIDDLE!")
# elif bmi >= 22.0 and a >= 45 : 
#     print("Your BMI is", round(bmi, 2),". Your risk of heart diseases is HIGH!")

# from time import sleep
# remain = 180
# # while True : 
# while remain > 0 : 
#     print(remain, "seconds left.")
#     sleep(1)
#     remain -= 1   
# print("Ramen is ready!")

# def my_pow(x, y) : 
#     if y == 1 : 
#         return(x) 
#     if y != 1 : 
#         return(x * my_pow(x, y - 1))
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# print("Result:", my_pow(x, y))





# def my_pow(x, y) : 
#     x **= y
#     return x
  
# while True : 
#     y = int(input("Yen= "))
#     print("It is $",y / 108, sep="")

# import inflect
# l = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 11, 12]

# def num_to_str(x) : 
#     y = inflect.engine()
#     if x in l : 
#         return(y.number_to_words(x))     
#     else : 
#         l.append(x)
#         return(y.number_to_words(x))
# num_to_str(1000)

# vegetables = ['apple', 'tomato', 'orange']
# for s in vegetables : 
#         print(s + ' juice')

# l = [1, 3 , 5, 7, 9]
# sum = 0
# for x in l :          
#     sum += x 
# print(sum)

# def pyramid(x) : 
#     for i in range(x) : 
#         for j in range(x - i) : 
#                 print(end=' ')
#         for j in range(i) : 
#                 print('##',end='')
#         print()

# pyramid(5)


# def sqrt(x) : 
#     a = 0.5 * x 
#     b = 0.5 * (a + x/a)
#     while b != a : 
#         a = b 
#         b = 0.5 * (a + x/a)
#     return a
# print(sqrt(10))

# def week_to_str(w) : 
#     weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     return(weeks[w - 1])

# bowling = [[120,102,110], [132,126,120]]
# average = []
# result = 0
# for x in bowling : 
#     result = sum(x)/len(x)
#     average.append(result)
# print(average)

# while True : 
#     Omikuji = ['大吉','吉','中吉','小吉','末吉','凶']
#     n = int(input("Input your date of birth with 8 digits here: "))
#     print(Omikuji[n%6])

# def voting_right(a, y) : 
#     if (a >= 18 and y >= 2016) or (y < 2016 and a >= 20) : 
#         return True
#     else : 
#         return False

# def omit_s(text) : 
#     result = ""
#     for x in text : 
#         if x not in 'sS' : 
#             result += x
#     return(result)

# omit_s('assssqwqwissssdasa')

# Rock, Paper, Scissor

# import random
# wins = 0
# Round = 0
# c = ["r", "p", "s"]
# print("Welcome to the Rock, Paper, Scissor game ahihi!")
# print("Start!") 

# while True :
#     print("--------------------")
#     Round += 1
#     print("ROUND", Round)
#     player = input("Your choice: ")
#     computer = random.choice(c)
#     if player not in c : 
#         print("Invalid choice! Try again! ")
#     else : 
#         if (player == 'r' and computer == 'p') or (player == 'p' and computer == 's') or (player == 's' and computer == 'r') : 
#             print("Computer's choice:", computer)
#             print("You lose!")
#         elif (player == 'p' and computer == 'r') or (player == 's' and computer == 'p') or (player == 'r' and computer == 's') : 
#             print("Computer's choice:", computer)
#             print("You win!")
#             wins += 1
#         elif player == computer : 
#             print("Computer's choice:", computer)
#             print("Draw!")
#     # Winrate
#     if Round % 5 == 0 : 
#         print("You won", wins, "games")
#         print("Your winrate is", wins / 5 * 100, "%" )


#Sokoban 
def reset_map() : 
    map_start = [['*', '*', '*', '*', '*', '*', '*', '*', '*'],
                 ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
                 ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
                 ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
                 ['*', '*', ' ', '*', '*', ' ', ' ', ' ', '*'],
                 ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
                 ['*', ' ', ' ', ' ', ' ', '*', ' ', ' ', '*'],
                 ['*', ' ', ' ', ' ', ' ', '*', ' ', ' ', '*'],
                 ['*', '*', '*', '*', '*', '*', '*', '*', '*']
                 ]
    return map_start

def display_map(map_list) : 
    for i in range(0, len(map_list)) :
        for j in range(0, len(map_list[0])) : 
            print(map_list[i][j],end='')
        print('')
    print('--------------------------------------------------------')
def set_map(map_list, player) : 
    map_list[player[0]][player[1]] = 'P'
    map_list[7][4] = 'S'
    map_list[box[0]][box[1]] = 'B'

# obj can be player and box
def move_object(obj, command) :
  if move == 'd' : 
      next_obj = [obj[0] + 0, obj[1] + 1]
  elif move == 'w' : 
      next_obj = [obj[0] - 1, obj[1] + 0]
  elif move == 'a' : 
      next_obj = [obj[0] + 0, obj[1] - 1]
  elif move == 's' :
      next_obj = [obj[0] + 1, obj[1] + 0]
  return next_obj

# check player's position to give matched command
def check_position_player(player, box) :
  if map_list[player[0]][player[1]] == "*" or  map_list[box[0]][box[1]] == "*": 
      print("Cannot move...")
      return "Stop"
  elif player[0] == box[0] and player[1] == box[1]: 
      print("Moving the box...")
      return "move_box"  
  elif map_list[player[0]][player[1]] == "S" :
      print("Cannot move...")
      return "Stop"
  else:
    return "move"

# logic
def handle_position (command, player, box):
  next_player = move_object(player, command)
  next_box = [box[0], box[1]]
  result = {
    "box": box,
    "player": player 
  }
  if check_position_player(next_player, box) == "move_box":
    next_box = move_object(next_box, command)
    if map_list[next_box[0]][next_box[1]] != "*":
      result["box"] = next_box
      result["player"] = next_player
  elif check_position_player(next_player, box) == "move":
    result["player"] = next_player
  return result

map_list = reset_map()
player = [6, 3]
box = [4, 5]
set_map(map_list, player)
display_map(map_list)
while True : 
    move = input("Please input 'd' or 'a' or 'w' or 's': ")
    if move == 'd' : 
        info = handle_position('d', player, box)
        box = info['box']
        player = info['player']
    elif move == 'w' : 
        info = handle_position('w', player, box)
        box = info['box']
        player = info['player']
    elif move == 'a' : 
        info = handle_position('a', player, box)
        box = info['box']
        player = info['player']
    elif move == 's' :
        info = handle_position('s', player, box)
        box = info['box']
        player = info['player']

    map_list = reset_map()
    set_map(map_list, player)
    display_map(map_list)































































































