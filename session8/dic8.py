# Lặp lại bài 7 với key nhập từ bàn phím
d = {
    "Name" : "Phạm Hải Long",
    "Age" : 19,
    "Description" : "Chú ong chăm chỉ",
    "Hobby" : "Đọc sách"
}
k = input("Which key do you want to print? ")
while k not in ["Name", "Age", "Description", "Hobby"] :
    k = input("Invalid Key,Type again: ")
print(d[k])