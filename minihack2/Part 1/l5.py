# delete 1 element
print("Our color list: ")
l = [ "blue", "red", "teal", "green" ]
for i, color in enumerate(l) : 
    print(i + 1, ".", color, sep="")
d = input("Item to delete: ")
if d.isdigit() : 
    d = int(d)
    while d > len(l) - 1 : 
        d = int(input("Invalid Item ! Type again : "))
    l.pop(d)
    print("Our new color list: ")
    for i, color in enumerate(l) : 
        print(i + 1, ".", color, sep="")
else : 
    l.remove(d) 
    print("Our new color list: ")
    for i, color in enumerate(l) : 
        print(i + 1, ".", color, sep="")


