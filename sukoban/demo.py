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
x = 1
y = 1
m[x][y] = 'P'
for i in m :
    for c in i :
        print(c, end = " ")
    print()
 
while True:
  control = input("W A S D to move P: ").lower()
  if control == "w":
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
 
  elif control == "q":
    print("QUIT THE GAME!")
    break
 
  for i in m :
    for c in i :
        print(c, end = " ")
    print()