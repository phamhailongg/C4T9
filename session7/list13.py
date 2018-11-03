# Sử dụng list ở bài tập số 12, sửa một phần từ của list với vị trí và nội dung mới là do người dùng nhập vào
l = ['Spider Man', 'photography', 'music', 'Dragon Ball']
l[int(input("Position: "))] = input("Thing you like: ")
print(l)