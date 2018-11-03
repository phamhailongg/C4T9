# Viết chương trình cho người dùng nhập vào một tháng trong năm và in ra số ngày của tháng này
m = int(input("Month? "))
 
if m <= 7 :
    if m % 2 == 0 : 
        print("This month has 30 days")
    elif m == 1 : 
        print("This month has 31 days")
    else :
        print("This month has 31 days")
else : 
    if m % 2 == 1 : 
        print("This month has 30 days")
    elif m == 7  : 
        print("This month has 31 days")
    else : 
        print("This month has 31 days")
    
    