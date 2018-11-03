# Dựa vào chương trình đã tạo ở bài 1, tạo thêm một mục là “nhập lại mật khẩu” ô “mật khẩu” và ô “nhập lại mật khẩu” phải giống nhau, nếu khác nhau báo lỗi và bắt người dùng nhập lại.
print("Sign up")
a = input("Your account: ")
p1 = input("Your password: ")
e = input("Your email: ")
print("Next step!")
p2 = input("Retype your password: ")
while True : 
    if p1 != p2 :
        p2 = input("Password unmatched, type again: ")
    else : 
        print("Matched")
        break