# Tiếp tục làm việc với chương trình  đã tạo ở bài 1,2 kiểm tra xem email người dùng nhập vào có phải là 1 email hợp lệ không (có @, có dấu chấm...),  độ dài tối thiểu của mật khẩu phải lớn hơn 8 ký tự, bao gồm cả chữ vào số. nếu không có yêu cầu người dùng nhập lại.
import string
def num_n_alphabet(x):
    a = x.isalpha()
    b = x.isdigit()
    if a or b :
        return False
    else :
        return True

name = (input("Your account: "))
p = (input("Your password: "))
while (not num_n_alphabet(p)) or len(p) <= 8:
    p = input("Your password must have at least 8 characters in both numbers and letters, type again: ")

p2 = (input("Retype password: "))
while p2 != p :
    p2 = (input("Password unmatched, type again: "))
e = (input ("Your email: "))

def valid (s):
    if ("@" in s) and ("." in s):
        return True
    else :
        return False    
while not valid(e) :
    email = input("Email invalid, try again: ")
print("Successfully signed up!")
    