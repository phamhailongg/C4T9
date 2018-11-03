# Xoá một phần tử bất kỳ trong list ở bài 16, giá trị của phần tử này do người dùng nhập vào
l = ['Spider Man', 'photography', 'music', 'Dragon Ball']
r = input("Thing you wanna remove: ")
if r in l : 
    l.remove(r)
    print(l)
else : 
    print(r, "is not in the list")
