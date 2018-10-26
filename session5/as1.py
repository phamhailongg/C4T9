# Viết một phương trình kiểm tra tuổi 

yob = int(input("Your year of birth? "))
age = 2018 - yob
print(age)

# Nếu tuổi người dùng lớn hơn 14, hiện ra thông báo "Mời bạn xem video".

if age > 14 :
    print("Mời bạn xem video ")
elif age == 4 :
    print("Tắt video")
else : 
    print("Bạn chưa đủ tuổi để xem video này")
