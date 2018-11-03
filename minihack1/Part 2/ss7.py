# Viết chương trình in ra một dãy số từ n đến 0, n > 0 do người dùng nhập vào
n = int(input("Number? "))
for i in reversed(range(n + 1)) :
    print(i)