# Xoá một phần tử bất kỳ trong list của bài 15, vị trí của phần tử này do người dùng nhập vào
l = ['Spider Man', 'photography', 'music', 'Dragon Ball']
choice = int(input("Position: "))
while choice > len(l) - 1 : 
    choice = int(input("No location found, again: "))
l.pop(choice)
print(l)