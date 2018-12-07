# game intro
print('''
[-] : Empty positions
[P] : Player
[B] : Box
[S] : Storage point
''')
# create map and first moving
m = [["-","-","-","-"] ,
    ["-","-","-","-"] ,
    ["-","-","-","-"] ,
    ["-","-","-","-"] ,
]
 
# initial Player Position
dx = 0
dy = 0
x = 1
y = 1
a = 2 
b = 2
gx = 2
gy = 1 #Gate (x,y)
m[gx][gy] = 'G'
m[a][b] = 'B'
m[x][y] = 'P'
for i in m :
    for c in i :
        print(c, end = " ")
    print()
# edge check 
if x == 3 : 
        dy == 0 
elif y == 0 : 
    dy == 0 
elif x == 0 : 
    dy = 0 
elif y == 3 : 
    dy = 0 
while True:
    # Move
    control = input("W A S D to move P: ").lower() 
    if  control == "w":
        m[x][y] = '-'
        x = x - 1
        m[x][y] = 'P'

    elif control == "s":
        m[x][y] = '-'
        x = x + 1
        m[x][y] = 'P'
    
    elif control == "a":
        m[x][y] = '-'
        y = y - 1
        m[x][y] = 'P'
    
    elif control == "d":
        m[x][y] = '-'
        y = y + 1
        m[x][y] = 'P'

    # Handle Exception
    if (gx == x and gy == y) : 
        m[x][y] = 'P'
    else:
        m[gx][gy] = 'G'
    
    # Edge check 
    
    if x == 3 : 
        dy == 0 
    elif y == 0 : 
        dy == 0 
    elif x == 0 : 
        dy = 0 
    elif y == 3 : 
        dy = 0 





    
    # Print Map
    for i in m :
        for c in i :
            print(c, end = " ")
        print()