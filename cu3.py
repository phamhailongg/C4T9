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

# obj có thể là box hay player, x, y là tọa độ
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

# Kiểm tra vị trí của player và đưa ra mệnh lệnh tương ứng
def check_position_player(player, box) :
  if map_list[player[0]][player[1]] == "*" or  map_list[box[0]][box[1]] == "*": 
      print("Cannot move...")
      return "stop"
  elif player[0] == box[0] and player[1] == box[1]: 
      print("Moving the box...")
      return "move_box"  
  elif map_list[player[0]][player[1]] == "S" :
      print("You win")
      return "win"
  else:
    return "move"

# Các logic liên quan đến xử lý vị trí nằm trong đây
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
