# Lặp lại bài 11 với key muốn xoá được nhập từ người dùng
d = {
    "Name" : "Phạm Hải Long",
    "Age" : 19,
    "Description" : "Chú ong chăm chỉ",
    "Hobby" : "Đọc sách"
}
k = input("Which key do you want to delete? ")
while k not in ["Name", "Age", "Description", "Hobby"] :
    k = input("Invalid key, Type again: ")
del d[k]
print(d)