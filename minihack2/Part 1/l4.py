# xem màu ở 1 vị trí cố định 
l = [ "blue", "red", "teal", "green" ]
p = int(input("Enter position: "))
while p > len(l) - 1 : 
    p = int(input("Invalid position! Type again : "))
print(l[p])