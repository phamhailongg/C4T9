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

def move_object(player,x, y) : 
    next_player = [player[0] + x, player[1] + y]
    if map_list[next_player[0]][next_player[1]] == "*" : 
        print("Cannot move...")
        return False
    player[0] = next_player[0]
    player[1] = next_player[1]
    return True
map_list = reset_map()
player = [6, 3]
set_map(map_list, player)
display_map(map_list)
while True : 
    print(player[0])
    move = input("Please input 'd' or 'a' or 'w' or 's': ")
    if move == 'd' : 
        flag = move_object(player, 0, 1)
    elif move == 'w' : 
        flag = move_object(player, -1, 0)
    elif move == 'a' : 
        flag = move_object(player, 0, -1)
    elif move == 's' :
        flag = move_object(player, 1, 0)
    else : 
        flag = False
    if flag : 
        map_list = reset_map()
        set_map(map_list, player)
        display_map(map_list)