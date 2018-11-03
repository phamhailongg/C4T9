# Viết chương trình cho người dùng nhập vào một số rồi in ra cho biết số này có phải là số chẵn hay không
n = int(input("Number? "))

if n % 2 == 0 : 
    print("This number is even!")
else : 
    print("This number is odd!")