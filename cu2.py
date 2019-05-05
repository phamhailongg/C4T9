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
# def move_box(box, x, y) : 
#     next_box = [box[0] + x, box[1] + y]
#     if map_list[next_player[0]][next_player[1]] == "B" : 
#         return False
def move_object(player,x, y) : 
    next_player = [player[0] + x, player[1] + y]
    # next_box = [box[0] + x, box[1] + y]
    if map_list[next_player[0]][next_player[1]] == "*" : 
        print("Cannot move...")
        return False
    elif map_list[next_player[0]][next_player[1]] == "B" : 
        print("Moving the box...")
        return False
    def move_box(box, a, b) :
        next_box = [box[0] + a, box[1] + b]
        if map_list[next_box[0]][next_box[1]] == "*" : 
            print("Cannot move...")
            return False
        elif map_list[next_box[0]][next_box[1]] == "S" : 
            print("Cannot move...")
            return False    
        
        return True
        
    if map_list[next_player[0]][next_player[1]] == "S" :
        print("Cannot move...")
        return False
    player[0] = next_player[0]
    player[1] = next_player[1]
    return True
map_list = reset_map()
player = [6, 3]
box = [4, 5]
set_map(map_list, player)
display_map(map_list)
while True : 
    move = input("Please input 'd' or 'a' or 'w' or 's': ")
    if move == 'd' : 
        flag1 = move_object(player, 0, 1)
        flag2 = move_box(box, 0, 1)
    elif move == 'w' : 
        flag1 = move_object(player, -1, 0)
    elif move == 'a' : 
        flag1 = move_object(player, 0, -1)
    elif move == 's' :
        flag1 = move_object(player, 1, 0)
    else : 
        flag1 = False
    if flag1 : 
        map_list = reset_map()
        set_map(map_list, player)
        display_map(map_list)